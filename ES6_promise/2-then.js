export default function handleResponseFromAPI(promise) {
  promise.then(function (response, error) {
    console.log('Got a response from the API');
    return { status: 200, body: 'success' };
    if (error) {
      console.error(error);
      return new Error()
    }
  });
}
