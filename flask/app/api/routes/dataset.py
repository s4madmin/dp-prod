"""
APIs to handle queries to individual datasets - ie. where the dataset id is known, 
and we want to fetch sample table or expression matrix.
/api/dataset.
"""
import json, os, pandas
from flask import request, Response, Blueprint
from app.api.models import datasets
from app.api.models import datasets
from flask_restplus import Resource, Api
from app import dataset_name_space, dataset_expression_name_space, api_app
from app.site.routes.api_login import token_required
from flask_jwt import jwt_required, JWT


module = Blueprint('dataset', __name__)


@dataset_name_space.route("/<int:datasetId>/<string:dataType>")	# This is how you can define your API in the swagger documentation. 
class DatasetClass(Resource):

    @api_app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self, datasetId, dataType):
        """
        Returns samples or metadata files for a dataset, expects: {dataset_id}/{data_type} where data_type is either 'samples' or 'metadata'.
        """
        ds = datasets.Dataset(datasetId)
        json_string = ds.isPrivate()
        json_object = json.loads(json_string)
        result = json_object[0]

        if result['datasets'][0]['private'] == True:
            return Response("Error: Private dataset", mimetype="text/tsv", headers={"Content-disposition": datasetId})

        if dataType=="samples":
            filename = 'attachment; filename=' + 'dataset_id_' + str(datasetId) + '_samples' + '.csv'
            json_string = ds.sampleTable().set_index("sample_id").to_csv()
            result = Response(json_string, mimetype="text/csv", headers={"Content-disposition": filename})
            return result
        
        elif dataType=="metadata":
            result = ds.metadataTable()
            return result   

@dataset_expression_name_space.route("/<int:datasetId>/<string:key>")
class DatasetExpressionClass(Resource):

    @api_app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self, datasetId, key):
        """
        Returns expression files for a dataset, expects: {dataset_id}/{string} where string is either 'genes' or 'raw'.
        """
        dataType = "expression"
        key = key
        ds = datasets.Dataset(datasetId)
        json_string = ds.isPrivate()
        json_object = json.loads(json_string)
        result = json_object[0]

        if result['datasets'][0]['private'] == True:
            return Response("Error: Private dataset", mimetype="text/tsv", headers={"Content-disposition": datasetId})

        json_string = ds.expressionMatrix(key=key).to_json(orient="split")
        result = Response(json_string, mimetype="text/csv", headers={"Content-disposition": key})
        return result
            

@module.route('/dataset/<int:datasetId>/<string:dataType>', methods=['GET', 'POST'])
@token_required
def getTable(datasetId, dataType):

    ds = datasets.Dataset(datasetId)
    json_string = ds.isPrivate()
    json_object = json.loads(json_string)
    result = json_object[0]

    if result['datasets'][0]['private'] == True:
        return Response("Error: Private dataset", mimetype="text/tsv", headers={"Content-disposition": datasetId})

    if dataType=="samples":
        filename = 'attachment; filename=' + 'dataset_id_' + str(datasetId) + '_samples' + '.csv'
        json_string = ds.sampleTable().set_index("sample_id").to_csv()
        result = Response(json_string, mimetype="text/csv", headers={"Content-disposition": filename})

    elif dataType=="metadata":
        result = ds.metadataTable()

    elif dataType=="expression":
        print("You chose expression")

    return result


@module.after_request  # Necessary to add the response headers for comms back to the UI. Add only authorized front end applications, example: https://ui-dp.stemformatics.org
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,PUT,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response



