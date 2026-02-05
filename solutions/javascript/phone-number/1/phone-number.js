
  export const clean = (str) => {
  if (/[a-zA-Z]/.test(str)) {
    throw new Error("Letters not permitted");
  }

  if (/[^0-9\s().+-]/.test(str)) {
    throw new Error("Punctuations not permitted");
  }

  let num = str.replace(/\D/g, "");

  if (num.length < 10) {
    throw new Error("Must not be fewer than 10 digits");
  }

  if (num.length > 11) {
    throw new Error("Must not be greater than 11 digits");
  }

  if (num.length === 11) {
    if (num[0] !== "1") {
      throw new Error("11 digits must start with 1");
    }
    num = num.slice(1); 
  }

  

  if (num[0] === "0") throw new Error("Area code cannot start with zero");
  if (num[0] === "1") throw new Error("Area code cannot start with one");

  if (num[3] === "0") throw new Error("Exchange code cannot start with zero");
  if (num[3] === "1") throw new Error("Exchange code cannot start with one");

  return num;
};



