// 0-promise.js

export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // You can resolve with any value, for example a string
    resolve("Success");
  });
}
