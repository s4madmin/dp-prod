![logo](https://dataportal-data.s3-ap-southeast-2.amazonaws.com/static/images/test_logo.PNG)
  
[![Build Status](https://travis-ci.com/s4madmin/dp-prod.svg?branch=master)](https://travis-ci.com/s4madmin/dp-prod)
  
# Stemformatics Dataportal API
  
Source code for the [Stemformatics Dataportal](https://api.stemformatics.org/). The dataportal is a centralised API and data store of all the datasets contained in Stemformatics. The API facilitates 
external access to both public and private datasets that exist in [stemformatics](https://www.stemformatics.org/).
  
  
#### See [Dataportal-documentation](http://dataportal-documentation.s3-website-ap-southeast-2.amazonaws.com/ "Documentation")
  
## Getting Started
  
#### Dev/Testing:
  
If using a development env like conda, you should first install all the dependencies in the requirements.txt file. You can run an adhoc, non-production grade instance using "python run.py"
  
#### Docker:
Load any/all your environment variables into the cloned repo location. The simplest way to do this is to use a .env file, but you can run export VAR=VALUE if you like. If you are using a .env file, run 
the load_vars.sh script to automate loading the environment variables.
  
Start the docker build:
  
``` docker-compose up ```
  
Once the build completes you will need to load the PSQL and MongoDB data. There is a script included in the repo called "load_data.sh". This script downloads the appropriate dump files from an AWS S3 
bucket location, the url for which will be contained in environment variables or .env file. If you are not authorised to download a test version of this data, you will need to provide your own. See the 
[documentation](http://dataportal-documentation.s3-website-ap-southeast-2.amazonaws.com/) above for how to initialise the data.
  
#### Testing
  
cd to the directory containing the test files to manually run tests: ``` python -m unittest ```
  
#### Built With
  
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The framework used * [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) - API Documentation * 
[Mongo](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_apac_australia_search_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&gclid=Cj0KCQjwy6T1BRDXARIsAIqCTXo10E_rTqydYPjnE4viNcoI14ctwUAH6QsJvCDLS4LyRC6pTYBIAjwaAhlSEALw_wcB) 
- Metadata Database * [PostgreSQL](https://www.postgresql.org/) - Used for sample storage and auth
  
  
## Versioning
  
See the [documentation](http://dataportal-documentation.s3-website-ap-southeast-2.amazonaws.com/) for versioning information.
  
## Authors
  
* **Jack Bransfield** - Software Engineer, Stemformatics CSCS * **Jarny Choi** - Bioinformatician, Stemformatics CSCS
  
See also the list of [contributors](http://dataportal-documentation.s3-website-ap-southeast-2.amazonaws.com/) who participated in this project.
# Contributor Covenant Code of Conduct
## Our Pledge
We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, 
ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and 
orientation. We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.
## Our Standards
Examples of behavior that contributes to a positive environment for our community include: * Demonstrating empathy and kindness toward other people * Being respectful of differing opinions, viewpoints, 
and experiences * Giving and gracefully accepting constructive feedback * Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience * Focusing on what is best not just for us as individuals, but for the
  overall community Examples of unacceptable behavior include: * The use of sexualized language or imagery, and sexual attention or
  advances of any kind * Trolling, insulting or derogatory comments, and personal or political attacks * Public or private harassment * Publishing others' private information, such as a physical or 
email
  address, without their explicit permission * Other conduct which could reasonably be considered inappropriate in a
  professional setting
## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem 
inappropriate, threatening, offensive, or harmful. Community leaders have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions 
that are not aligned to this Code of Conduct, and will communicate reasons for moderation decisions when appropriate.
## Scope
This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public spaces. Examples of representing our community include 
using an official e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event.
## Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible for enforcement at [INSERT CONTACT METHOD]. All complaints will be reviewed and 
investigated promptly and fairly. All community leaders are obligated to respect the privacy and security of the reporter of any incident.
## Enforcement Guidelines
Community leaders will follow these Community Impact Guidelines in determining the consequences for any action they deem in violation of this Code of Conduct:
### 1. Correction
**Community Impact**: Use of inappropriate language or other behavior deemed unprofessional or unwelcome in the community. **Consequence**: A private, written warning from community leaders, providing 
clarity around the nature of the violation and an explanation of why the behavior was inappropriate. A public apology may be requested.
### 2. Warning
**Community Impact**: A violation through a single incident or series of actions. **Consequence**: A warning with consequences for continued behavior. No interaction with the people involved, including 
unsolicited interaction with those enforcing the Code of Conduct, for a specified period of time. This includes avoiding interactions in community spaces as well as external channels like social media. 
Violating these terms may lead to a temporary or permanent ban.
### 3. Temporary Ban
**Community Impact**: A serious violation of community standards, including sustained inappropriate behavior. **Consequence**: A temporary ban from any sort of interaction or public communication with 
the community for a specified period of time. No public or private interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, is allowed during 
this period. Violating these terms may lead to a permanent ban.
### 4. Permanent Ban
**Community Impact**: Demonstrating a pattern of violation of community standards, including sustained inappropriate behavior, harassment of an individual, or aggression toward or disparagement of 
classes of individuals. **Consequence**: A permanent ban from any sort of public interaction within the community.
## Attribution
This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 2.0, available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html. Community Impact Guidelines 
were inspired by [Mozilla's code of conduct enforcement ladder](https://github.com/mozilla/diversity). [homepage]: https://www.contributor-covenant.org For answers to common questions about this code 
of conduct, see the FAQ at https://www.contributor-covenant.org/faq. Translations are available at https://www.contributor-covenant.org/translations.
## License
  
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
