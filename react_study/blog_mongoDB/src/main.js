require("dotenv").config();
import Koa from "koa";
import Router from "koa-router";
import bodyParser from "koa-bodyparser";
import mongoose from "mongoose";

import api from "./api";
// import createFakeData from "./createFakeData";

const { PORT, MONGO_URI } = process.env;

mongoose
  .connect(MONGO_URI)
  .then(() => {
    console.log("Connected to MongoDB");
    // createFakeData();
  })
  .catch((e) => {
    console.error(e);
  });

//const api = require("./api");

const app = new Koa();
const router = new Router();

router.use("/api", api.routes()); // api 라우트 적용

app.use(bodyParser());

app.use(router.routes()).use(router.allowedMethods());

const port = PORT || 4000;
app.listen(port, () => {
  console.log("Listening to port %d", port);
});
