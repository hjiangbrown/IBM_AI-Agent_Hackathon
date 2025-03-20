import { createAmazonBedrock } from '@ai-sdk/amazon-bedrock';
import { BackendClient } from '../../../backend/client.js';

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class AmazonBedrockClient extends BackendClient {
  static {
    __name(this, "AmazonBedrockClient");
  }
  create() {
    return createAmazonBedrock({
      ...this.settings
    });
  }
}

export { AmazonBedrockClient };
//# sourceMappingURL=client.js.map
//# sourceMappingURL=client.js.map