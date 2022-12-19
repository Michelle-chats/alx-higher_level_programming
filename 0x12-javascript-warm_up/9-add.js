#!/usr/bin/node
function add (a, b) {
	const c = a + b;
	onsole.log(c);
}

add(Number(process.argv[2]), Number(process.argv[3]));
