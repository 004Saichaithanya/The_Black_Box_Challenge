# 🔍 Black Box API Decoder (Flask)

This project is a reverse-engineering challenge involving a set of undocumented API endpoints hosted on a simulated malfunctioning system. Each endpoint behaves unpredictably with no official documentation, and the task was to deduce their hidden logic through carefully crafted requests and analysis of responses.

---

## 📦 Tech Stack

- **Python 3**
- **Flask** (for building the local API)
- **Postman** / **curl** (for testing HTTP requests)

---

## 📖 API Endpoints & Their Hidden Secrets

---

### 📌 `POST /data`

**🔒 Hidden Behavior:**  
Encodes the input string to Base64.

**📥 Example Input:**
```json
{ "data": "hello" }
````

**📤 Example Output:**

```json
{ "result": "aGVsbG8=" }
```

---

### 📌 `GET /time`

**🔒 Hidden Behavior:**
Returns the remaining seconds to a preset future timestamp (95 days from server start). Constantly decrements with time.

**📤 Example Output:**

```json
{ "result": 8163512 }
```

---

### 📌 `POST /glitch`

**🔒 Hidden Behavior:**

* If input string’s length is **even** → randomly shuffles its characters.
* If **odd** → reverses the string.

**📥 Example Input:**

```json
{ "data": "abcd" }
```

**📤 Possible Output (even length):**

```json
{ "result": "cbad" }
```

**📥 Example Input:**

```json
{ "data": "abcde" }
```

**📤 Output (odd length):**

```json
{ "result": "edcba" }
```

---

### 📌 `POST /zap`

**🔒 Hidden Behavior:**
Removes all non-alphabetic characters from the string.

**📥 Example Input:**

```json
{ "data": "abc123!!" }
```

**📤 Output:**

```json
{ "result": "abc" }
```

---

### 📌 `POST /alpha`

**🔒 Hidden Behavior:**
Returns `true` if the first character is an alphabet letter, else `false`.

**📥 Example Input:**

```json
{ "data": "hello" }
```

**📤 Output:**

```json
{ "result": true }
```

**📥 Example Input:**

```json
{ "data": "123abc" }
```

**📤 Output:**

```json
{ "result": false }
```

---

### 📌 `POST /fizzbuzz`

**🔒 Hidden Behavior (Initial Decoded Logic):**

* If `data` is **not a list** → returns `false`
* If `data` is a **list with even length** → returns the list itself
* elements in the list can be any datatype !!
* If `data` is a **list with odd length** → returns `false`

> ⚠️ **Note:** The endpoint name is a complete decoy — there’s no actual fizzbuzz number check happening.

**📥 Example Input:**

```json
{ "data": [1, 2, 3, 4] }
```

**📤 Output:**

```json
{ "result": [1, 2, 3, 4] }
```

**📥 Example Input:**

```json
{ "data": [3, 5, 7] }
```

**📤 Output:**

```json
{ "result": false }
```

**📥 Example Input:**

```json
{ "data": "FizzBuzz" }
```

**📤 Output:**

```json
{ "result": false }
```

---
### 📌 `POST /fizzbuzz`  (Later Debugging it changed behaviour)

**Behavior:**
**After exhaustive testing and analysis, it is determined that this endpoint is a deliberate decoy.**

**Summary:**

* Accepts a JSON array as input.
* Regardless of list length, contents, data types, numerical patterns, or combinations, it **consistently returns `false`.**
* No condition, including classic FizzBuzz checks (divisibility by 3 or 5), empty lists, mixed or uniform types, or any numerical pattern triggers a different response.

**Verdict:**
Likely implemented intentionally as a dead-end endpoint to consume debugging time and serve as a distraction within the challenge design.

**Example:**

```json
{ "data": [3, 5, 15] }
```

➡️ `{ "result": false }`

```json
{ "data": [] }
```

➡️ `{ "result": false }`

---

## ⚙️ How to Run

1️⃣ Install Flask:

```bash
pip install Flask
```

2️⃣ Run the server:

```bash
python app.py
```

3️⃣ Use **Postman** or **curl** to test the endpoints locally at:

```
http://127.0.0.1:5000/
```

---

## 🚧 Challenges Faced

* **No documentation available:** Required observing behavior purely through input/output experimentation.
* **Misleading endpoint names:** Especially `/fizzbuzz`, which suggested classic fizzbuzz checks but actually operated based on list length.
* **Type and structure-dependent behaviors:** Many endpoints behaved differently for strings, numbers, and arrays.
* **Hidden conditions without hints:** Some endpoints required extensive trial and error to reveal their internal rules.
* **Obscure logic gates:** Like `/glitch` shuffling or reversing based on string length parity.

---

## 📌 Conclusion

This was an engaging black-box API decoding exercise, blending debugging, payload crafting, pattern deduction, and creative problem-solving. It effectively simulates real-world reverse engineering scenarios of undocumented or obfuscated APIs.

---

## 👑 Reverse Engineering Completed ✅
