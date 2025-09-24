//
// This is only a SKELETON file for the 'Transpose' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const transpose = (inputList) => {
  let result = []
      for (let i=0; i<inputList.length;i++){
          for (let j = 0; j<inputList[i].length;j++){
            let rowLength = 0;
            let element = inputList[i][j];
            
            if (result[j]){
              rowLength = result[j].length;
            }
            if (i > rowLength){
              element = element.padStart(i-rowLength+1,' ');
            }
            result[j]?result[j]+= element : result[j]=element;
        }
      }
  console.log(inputList);
  return result;
};
