function test(name){
  var result = ""
  for (var i = name.length-1; i >= 0; i--){
    result += name[i]
  } 
  return result
}

console.log(test("Raditya Fauzan"))