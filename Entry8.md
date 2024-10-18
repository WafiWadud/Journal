# spinner in node js with no dependencies and examples

So, after what felt like an eternity, an idea struck me - What if i made a spinner using nothing but escape codes?

Well, without further ado, let's hop into the code

```javascript
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const clearScreen = () => process.stdout.write("\x1b[H\x1b[2J\x1b[3J");
import readline from "readline"; // only needed for the examples

clearScreen(); // For consistency's sake

function spinner() {
  const str = "-\b|\b/\b-\b\\\b|\b/\b"; // it goes like - | / - \ | /
  let i = 0;
  let isRunning = true;

  const stop = () => {
    clearScreen(); // So that it doesn't look bad
    isRunning = false;
  };

  // Separate iife so that we can return the stop function.
  (async () => {
    while (isRunning) {
      if (i === str.length) {
        i = 0;
      }
      process.stdout.write(str[i]);
      i += 1;
      await delay(350);
    }
  })();

  return stop;
}

async function interactiveExample() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  console.log("Starting spinner... Press Enter to stop it");
  const stopSpinner = spinner();

  // Wait for user to press Enter
  await new Promise((resolve) => {
    rl.once("line", () => {
      stopSpinner();
      console.log("\nSpinner stopped!");
      rl.close();
      resolve();
    });
  });
}

async function simulateLoading() {
  console.log("Loading data...");
  const stopSpinner = spinner();

  try {
    // Simulate some async work
    await delay(5000);
    console.log("\nFirst step complete");

    await delay(2500);
    console.log("\nSecond step complete");

    await delay(1000);
    console.log("\nDone loading!");
  } finally {
    stopSpinner();
  }
}

// Run the examples sequentially
await interactiveExample();
await simulateLoading();
```
