function isPalindrome(str) {
    return str === str.split('').reverse().join('');
}
console.log(isPalindrome("malayalam") ? "malayalam is a palindrome" : "malayalam is not a palindrome");