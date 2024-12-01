import fs from "fs";
import {Base64} from "js-base64";

let codeRequest = {
    command: "code-review",
    data: Base64.encode(fs.readFileSync("./new.py")),
};

let request = await fetch("http://localhost:8000/request", {
    method: "POST",
    headers: {
        'Content-Type': 'application/json' // Set Content-Type to application/json
    },
    body: JSON.stringify(codeRequest),
});

let response = await request.json();

console.log(response.answer);
