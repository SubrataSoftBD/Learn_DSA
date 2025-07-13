main(){

arrayData(List array){

  for(var newData in array){
    print(newData);
  }

 for (var name in array){
  for (var newName in  array){
    print("${name} + ${newName}"); // Adding loop more then n3 or n4 the time complexity is slow
  }
 }

 // 0(n + n2) = 0(n2)
 
}

arrayData([1,2,3,4,5,6,7,8,9,10,11,12,13]);




}