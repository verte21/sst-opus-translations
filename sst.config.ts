import { SSTConfig } from "sst";
import { Lambdas } from "./stacks/Lambdas";
import { API } from "./stacks/Api";

export default {
  config(_input) {
    return {
      name: "easynmt-opus-translation",
      region: "eu-west-1",
    };
  },
  stacks(app) {
    app.stack(Lambdas);
    app.stack(API);
  },
} satisfies SSTConfig;
