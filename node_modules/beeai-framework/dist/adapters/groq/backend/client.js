import { createGroq } from '@ai-sdk/groq';
import { BackendClient } from '../../../backend/client.js';
import { getEnv } from '../../../internals/env.js';

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class GroqClient extends BackendClient {
  static {
    __name(this, "GroqClient");
  }
  create() {
    return createGroq({
      baseURL: getEnv("GROQ_API_BASE_URL"),
      apiKey: getEnv("GROQ_API_KEY"),
      ...this.settings
    });
  }
}

export { GroqClient };
//# sourceMappingURL=client.js.map
//# sourceMappingURL=client.js.map