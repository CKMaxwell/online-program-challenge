// Is Sator Square?
/*
Your Task
Please help Farmer Arepo by inspecting each tablet to see if it forms a valid Sator Square!
*/
// https://www.codewars.com/kata/5cb7baa989b1c50014a53333/train/typescript

export function isSatorSquare(tablet: string[][]): boolean {
  let arr_length = tablet.length;
  let flag_down = false;
  let flag_up = false;
  let flag_reverse = false;
  for (let i = 0; i < arr_length; i += 1) {
    flag_down = false;
    flag_up = false;
    flag_reverse = false;
    let word = tablet[i];
    // console.log(`word = ${word}`);
    // 處理down
    for (let down_index = 0; down_index < arr_length; down_index += 1) {
      let down = [];
      for (let j = 0; j < arr_length; j += 1) {
        down.push(tablet[j][down_index]);
      }
      // console.log(`down=${down}`);
      // 注意：js陣列比較的是「記憶體位置」，不是內容。直接down == word會是false
      if (down.join("") == word.join("")) {
        flag_down = true;
        break;
      }
    }
    if (!flag_down) {
      flag_down = false;
      flag_up = false;
      flag_reverse = false;
      break;
    }
    // 處理up
    for (let up_index = 0; up_index < arr_length; up_index += 1) {
      let up = [];
      for (let j = arr_length - 1; j >= 0; j -= 1) {
        up.push(tablet[j][up_index]);
      }
      // console.log(`up=${up}`);
      if (up.join("") == word.join("")) {
        flag_up = true;
        break;
      }
    }
    if (!flag_up) {
      flag_down = false;
      flag_up = false;
      flag_reverse = false;
      break;
    }
    // 處理reverse
    for (let rev_index = 0; rev_index < arr_length; rev_index += 1) {
      let rev = [];
      for (let j = arr_length - 1; j >= 0; j -= 1) {
        rev.push(tablet[rev_index][j]);
      }
      // console.log(`rev=${rev}`);
      if (rev.join("") == word.join("")) {
        flag_reverse = true;
        break;
      }
    }
    if (!flag_reverse) {
      flag_down = false;
      flag_up = false;
      flag_reverse = false;
      break;
    }
  }
  if (flag_up && flag_down && flag_reverse) {
    return true;
  } else {
    return false;
  }
}
