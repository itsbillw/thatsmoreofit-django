function bloodsugarConverterA1C(valNum) {
  valNum = parseFloat(valNum);
  document.getElementById("outputEAG").innerHTML=(valNum*28.7)-46.7;
}

function bloodsugarConverterEAG(valNum) {
  valNum = parseFloat(valNum);
  document.getElementById("outputA1C").innerHTML=(valNum+46.7)/28.7;
}
