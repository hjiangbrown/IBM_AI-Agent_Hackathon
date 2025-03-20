'use strict';

var amazonBedrock = require('@ai-sdk/amazon-bedrock');
var client_cjs = require('../../../backend/client.cjs');

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class AmazonBedrockClient extends client_cjs.BackendClient {
  static {
    __name(this, "AmazonBedrockClient");
  }
  create() {
    return amazonBedrock.createAmazonBedrock({
      ...this.settings
    });
  }
}

exports.AmazonBedrockClient = AmazonBedrockClient;
//# sourceMappingURL=client.cjs.map
//# sourceMappingURL=client.cjs.map