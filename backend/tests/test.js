import {Base64} from "js-base64";

let codeRequest = {
    command: "text-review",
    data: Base64.encode("print(hello world)\n\nuser_input = input\n\nprint(user_input)"),
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
