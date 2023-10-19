## Poetry

### Add library

common: `poetry add chalice`

dev only: `poetry add --group dev pytest`

vscode ユーザの DevContainer 内では sudo じゃないと `/usr/local/bin/python` にインストールできない. 以下実行後に `sudo poetry add <package-name>` すればおｋ.

`sudo poetry config virtualenvs.create false`

### Export dependences

common: `poetry export -o requirements.txt`

dev only: `poetry export --with dev -o requirements-dev.txt`

### AWS CLI

**Configuration with SSO**

`aws configure sso`

[参考) DevelopersIO (produced by Classmethod) AWS CLI を AWS IAM Identity Center(SSO)で認証させるには?](https://dev.classmethod.jp/articles/aws-cli-for-iam-identity-center-sso/)

**Deploy CloudFormation Stack**

`aws cloudformation deploy --stack-name chaliceOtameshi --template-file ./aws-cfn/cognito.yaml --parameter-overrides AuthName=chaliceOtameshi --capabilities CAPABILITY_IAM --profile chalice-otameshi`
