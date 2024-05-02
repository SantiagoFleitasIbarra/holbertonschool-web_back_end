export default function appendToEachArrayValue(array, appendString) {
  const list = [];
  for (let value of array) {
    list.push(appendString + value);
  }
  return list;
}
