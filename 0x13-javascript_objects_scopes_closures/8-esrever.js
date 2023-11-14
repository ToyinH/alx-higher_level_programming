#!/usr/bin/node
exports.esrever = function (list) {
  let i;

  const size = list.length;
  for (i = 0; i < size / 2; i++) {
    const temp = list[i];
    list[i] = list[size - 1 - i];
    list[size - 1 - i] = temp;
  }
  return list;
};
