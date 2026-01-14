// Credit Card Mask
/*
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
*/
// https://www.codewars.com/kata/5412509bd436bd33920011bc/train/javascript

// return masked string
function maskify(cc) {
  let mask_string = '';
  if (cc.length <= 4) {
    mask_string = cc;
    return mask_string;
  } else {
    for (let i = 0; i < cc.length - 4; i += 1) {
      mask_string += '#'
    }
    for (let j = cc.length - 4; j < cc.length; j += 1) {
        mask_string += cc[j]
    }
    return mask_string
  }
}

let sample_txt = "4556364607935616"
console.log(maskify(sample_txt))
