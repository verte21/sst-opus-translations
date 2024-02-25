import { Api, StackContext, use, useFunctions } from "sst/constructs";
import { Lambdas } from "./Lambdas";

export function API({ stack }: StackContext) {
  const { translationFn } = use(Lambdas);

  const api = new Api(stack, "translation-api", {
    routes: {
      "POST /api/translate/{languageCode}": {
        cdk: {
          function: translationFn,
        },
      },
    },
  });
}
