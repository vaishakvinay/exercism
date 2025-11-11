//
// This is only a SKELETON file for the 'Diffie Hellman' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


export class DiffieHellman {
  constructor(p, g) {
    if (p <= 1 || g <= 1) {
      throw new Error('p and g must be greater than 1');
    }
    if (!this.isPrime(p) || !this.isPrime(g)) {
      throw new Error('p and g must be prime numbers');
    }

    this.p = p;
    this.g = g;
  }

  isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  getPublicKey(privateKey) {
    if (privateKey<=1 || privateKey>=this.p) throw new Error();
    return (this.g**privateKey)% this.p ;
  
  }

  getSecret(theirPublicKey, myPrivateKey) {
   return (theirPublicKey** myPrivateKey)% this.p;
  }

 static getPrivateKey(p) {

    return Math.floor((Math.random() * (p - 2)) + 2);
  }
}
