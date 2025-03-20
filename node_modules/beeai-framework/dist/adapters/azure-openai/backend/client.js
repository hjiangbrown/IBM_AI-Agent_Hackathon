import { createAzure } from '@ai-sdk/azure';
import { getEnv } from '../../../internals/env.js';
import { BackendClient } from '../../../backend/client.js';

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class AzureOpenAIClient extends BackendClient {
  static {
    __name(this, "AzureOpenAIClient");
  }
  create(options) {
    return createAzure({
      ...options,
      apiKey: options?.apiKey || getEnv("AZURE_OPENAI_API_KEY"),
      baseURL: options?.baseURL || getEnv("AZURE_OPENAI_API_ENDPOINT"),
      resourceName: options?.resourceName || getEnv("AZURE_OPENAI_API_RESOURCE"),
      apiVersion: options?.apiVersion || getEnv("AZURE_OPENAI_API_VERSION")
    });
  }
}

export { AzureOpenAIClient };
//# sourceMappingURL=client.js.map
//# sourceMappingURL=client.js.map