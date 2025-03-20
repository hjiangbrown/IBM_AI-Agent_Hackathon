'use strict';

var azure = require('@ai-sdk/azure');
var env_cjs = require('../../../internals/env.cjs');
var client_cjs = require('../../../backend/client.cjs');

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class AzureOpenAIClient extends client_cjs.BackendClient {
  static {
    __name(this, "AzureOpenAIClient");
  }
  create(options) {
    return azure.createAzure({
      ...options,
      apiKey: options?.apiKey || env_cjs.getEnv("AZURE_OPENAI_API_KEY"),
      baseURL: options?.baseURL || env_cjs.getEnv("AZURE_OPENAI_API_ENDPOINT"),
      resourceName: options?.resourceName || env_cjs.getEnv("AZURE_OPENAI_API_RESOURCE"),
      apiVersion: options?.apiVersion || env_cjs.getEnv("AZURE_OPENAI_API_VERSION")
    });
  }
}

exports.AzureOpenAIClient = AzureOpenAIClient;
//# sourceMappingURL=client.cjs.map
//# sourceMappingURL=client.cjs.map