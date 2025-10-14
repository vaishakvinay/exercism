//
// This is only a SKELETON file for the 'Raindrops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = (num) => {
  if (num%7==0 &&num%3!=0 && num%5!=0){
    return "Plong";
  }
  else if(num%7!=0 && num%3==0 && num%5!=0){
    return "Pling";
  }
    else if(num%7!=0 && num%3!=0 && num%5==0){
    return "Plang";
    }
     else if(num%7==0 && num%3==0 && num%5!=0){
    return "PlingPlong";
    }
     else if(num%7==0 && num%3!=0 && num%5==0){
    return "PlangPlong";
     }
    else if(num%7!=0 && num%3==0 && num%5==0){
    return "PlingPlang";
    }
     else if(num%7==0 && num%3==0 && num%5==0){
    return "PlingPlangPlong";
     }
  else {
    return num.toString();
  }
  
};
