import { getEnv } from '../../../internals/env.js';
import { createVertex } from '@ai-sdk/google-vertex';
import { BackendClient } from '../../../backend/client.js';

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
class GoogleVertexClient extends BackendClient {
  static {
    __name(this, "GoogleVertexClient");
  }
  create() {
    return createVertex({
      ...this.settings,
      project: this.settings?.project || getEnv("GOOGLE_VERTEX_PROJECT"),
      baseURL: this.settings?.baseURL || getEnv("GOOGLE_VERTEX_ENDPOINT"),
      location: this.settings?.location || getEnv("GOOGLE_VERTEX_LOCATION")
    });
  }
}

export { GoogleVertexClient };
//# sourceMappingURL=client.js.map
//# sourceMappingURL=client.js.map