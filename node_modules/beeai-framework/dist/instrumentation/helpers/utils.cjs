'use strict';

var chat_cjs = require('../../backend/chat.cjs');

var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });
function assertLLMWithMessagesToPromptFn(instance) {
  return Boolean(instance && instance instanceof chat_cjs.ChatModel);
}
__name(assertLLMWithMessagesToPromptFn, "assertLLMWithMessagesToPromptFn");

exports.assertLLMWithMessagesToPromptFn = assertLLMWithMessagesToPromptFn;
//# sourceMappingURL=utils.cjs.map
//# sourceMappingURL=utils.cjs.map