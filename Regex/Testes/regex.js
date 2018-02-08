var target = "11a22b33c44d55e";

var exp = /(\d\d)(\w)/g; // 2 dígitos, 1 word char e após o / são as flags

if (exp.test(target)) {
	var result = null;
	while( result = exp.exec(target) ) {
		console.log(result);
		console.log(exp.lastIndex);
	}
} else {
	console.log("This pattern does not exist in the provided text");
}

target = "2018-02-08";

exp = /-/g;

console.log(target);
console.log(target.replace(exp, '/'));

var csv = '100,200-150,200;20';

exp = /[,;-]/;

var values = csv.split(exp);

console.log(values);

var codes = 'A121B12112C12212F12G01';
exp = /[A-Za-z]\d+/g;
values = codes.match(exp);
console.log(values);

// Ver também em HTML, num input dentro de um formulário, o atributo pattern