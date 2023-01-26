# Replicate DreamBooth API Weight Pusher

This [Cog](https://github.com/replicate/cog) model allows you to easily push trained model weights using the Replicate DreamBooth API. Simply feed in your input weights in the form of a zip file containing the trained model weights, and let the API do the rest. The trained model will then be pushed by cog and you will recieve your model version.

## Usage

1. First clone the repo and follow the instructions [here](https://replicate.com/docs/guides/push-a-model) to push your model to Replicate using Cog

You will receive a `version` of the new model you have created from Cog

Then use the [Replicate DreamBooth API](https://replicate.com/blog/dreambooth-api) to push a model with your trained weights.

You will need to pass the `url` of the zipped weights as the input for the Replicate DreamBooth API


```
curl -X POST \
    -H "Authorization: Token $REPLICATE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
            "input": {
                "instance_prompt": "$WEIGHTS_URL"
            },
            "model": "yourusername/yourmodel",
            "trainer_version": "$MODEL_VERSION",
            "webhook_completed": "https://example.com/dreambooth-webhook"
        }' \
    https://dreambooth-api-experimental.replicate.com/v1/trainings
```

The API will then call your webhook with a version of your trained model pushed to Replicate cluster that you can use in your application.

## More information

You can find more information about the DreamBooth API, including how to use it and example code, on our website at:
https://replicate.com/blog/dreambooth-api

### Note

Please check the API documentation for more details on the input format, endpoint and any other parameter that could be required.

