main(){





arrayData(List array, List<String> name){
  print("Hello World"); // Big 0(1)
  for (int i = 0; i < array.length; i++) { // Big 0(N) Linear array
    print("Data: ${array[i]}");

  }

  for (int i = 0; i < name.length; i++) { // Big 0(M) Linear array
    print("Data: ${name[i]}");

  }
  // O (N + M) = N

    print("After Hello World"); // Big 0(1)
}

  arrayData([12, 34, 5, 12, 6, 7, 8, 9, 0], ["Subrata", "Babu"]);

}