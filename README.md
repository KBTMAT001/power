# power
Description:
Allows users to calculate savings from distributed generation and for a service provider to tracker requests. 

Deployment:
All required files are within the public repo, including a Dockerfile to allow for containerisation and further deployment after changes have been made.

Modifications required:
ALLOWED_HOSTS
  Within hyperion/hyperion/settings.py the ALLOWED_HOSTS variable has been set to a wildcard value to allow for testing on VM. 
  This however compromises the website security in production deployment. 
  The variable is to be restricted to acceptable host addresses. 
