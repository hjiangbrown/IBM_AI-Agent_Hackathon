import { ClassConstructor } from '../internals/types.cjs';
import { ProviderName, ProviderDef } from './constants.cjs';
import '../internals/helpers/guards.cjs';

/**
 * Copyright 2025 IBM Corp.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

type FullModelName = `${ProviderName}:${string}`;
declare function parseModel(name: string): {
    providerId: "openai" | "azure" | "watsonx" | "ollama" | "google-vertex" | "amazon-bedrock" | "groq" | "dummy";
    modelId: string;
    providerDef: ProviderDef;
};
declare function loadModel<T>(name: ProviderName | FullModelName, type: "embedding" | "chat"): Promise<ClassConstructor<T>>;

export { type FullModelName, loadModel, parseModel };
