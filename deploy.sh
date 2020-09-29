#!/bin/bash
gcloud builds submit --tag "gcr.io/asksteve-mobile-86854/steve-dataflow:latest"

gcloud beta dataflow flex-template build gs://dataflow-staging-sea-1/steve-dataflow.json \
--image "gcr.io/asksteve-mobile-86854/steve-dataflow:latest" \
--sdk-language "PYTHON" \
--metadata-file "metadata.json"

