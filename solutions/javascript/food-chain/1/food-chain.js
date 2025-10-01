//
// This is only a SKELETON file for the 'Food Chain' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
 const animals = [
  {
    name: "fly",
    line: "I don't know why she swallowed the fly. Perhaps she'll die."
  },
  {
    name: "spider",
    line: `It wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "bird",
    line: `How absurd to swallow a bird!
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "cat",
    line: `Imagine that, to swallow a cat!
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "dog",
    line: `What a hog, to swallow a dog!
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "goat",
    line: `Just opened her throat and swallowed a goat!
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "cow",
    line: `I don't know how she swallowed a cow!
She swallowed the cow to catch the goat.
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.`
  },
  {
    name: "horse",
    line: `She's dead, of course!`
  }
];         
export class Song {
  verse(n) {
  const animal = animals[n - 1]; 
    return `I know an old lady who swallowed a ${animal.name}.\n${animal.line}\n`;
  }
  

  verses(start,end) {
    let result = '';
    for (let i = start; i <= end; i++) {
        result += this.verse(i);
        if (i < end) result += '\n';
    }
    return result + '\n';
}}
