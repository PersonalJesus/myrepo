#!/bin/bash
TOKEN="" #Token for gitlab api
ID= # ID for project
declare -A vars
vars[CI_REGISTRY_DEV_HOST]=''
vars[CI_REGISTRY_USER]=''
vars[CI_REGISTRY_PWD]=''
vars[CI_TECH_USER_NAME]=''
vars[CI_TECH_USER_PASS]=''
vars[PUSH_TOKEN]=''
vars[RUNNER]=''


for i in "${!vars[@]}"
do
    curl --location --request POST "https://gitlab.ru/api/v4/groups/$ID/variables" \
    --header "PRIVATE-TOKEN: $TOKEN" \
    --form "key="$i"" \
    --form "value="${vars[$i]}""
done
