//
// This is only a SKELETON file for the 'Protein Translation' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const codonMap = new Map([
  ["AUG", "Methionine"],
  ["UUU", "Phenylalanine"],
  ["UUC", "Phenylalanine"],
  ["UUA", "Leucine"],
  ["UUG", "Leucine"],
  ["UCU", "Serine"],
  ["UCC", "Serine"],
  ["UCA", "Serine"],
  ["UCG", "Serine"],
  ["UAU", "Tyrosine"],
  ["UAC", "Tyrosine"],
  ["UGU", "Cysteine"],
  ["UGC", "Cysteine"],
  ["UGG", "Tryptophan"],
  ["UAA", "STOP"],
  ["UAG", "STOP"],
  ["UGA", "STOP"]
]);

export const translate = (strand) => {
  if (!strand) return [];
let result=[];
  for (let i=0;i<strand.length;i+=3){
  let  codon = strand.slice(i,i+3);
  let  aminoAcid= codonMap.get(codon);
if (!aminoAcid) throw new Error("Invalid codon");
    if (aminoAcid === "STOP") break;
      result.push(aminoAcid);
      
    
  }
return result;
};
