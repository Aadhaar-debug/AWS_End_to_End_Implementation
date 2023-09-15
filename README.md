# AWS_End_to_End_Implementation
The repository contains the project files for a deployed web portal that leverages all the major services provided by the AWS cloud console.


Deployment :https://dev.duih274bf13ty.amplifyapp.com/

## The implementation uses 5 major AWS services namely, Lambda , Amplify , IAM , API Gateway and  Dynamo db
The site takes the input from the users at teh local level from where the inputs are sent onto the Lambda portal , from where the API gateway takes the data and appends it to the Dynamo DB schema.
The API gateway uses a secure tunnel using the AWS IAM and ensures the authenticity of the site.
Finally the Amplify hosts the entire site on the platform and assigns a domain name to the site to make it accessible to the world.
