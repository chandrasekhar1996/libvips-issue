FROM centos:7

WORKDIR /usr/src/app

RUN curl -sL https://rpm.nodesource.com/setup_14.x | bash -

RUN yum install -y nodejs

RUN yum install gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools -y

COPY . .

RUN npm ci && npm run ci-build

RUN rpmbuild --quiet --define "SOURCE_DIR /usr/src/app" --define "RELEASE 1.1" -bb my-app.spec