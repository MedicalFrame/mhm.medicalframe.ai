import fs from "node:fs";
import path from "node:path";

const root = path.resolve(new URL("../../", import.meta.url).pathname);
const outRoot = path.join(root, "brunch");
const queuePath = path.join(outRoot, "image_queue.json");

const [generatedDir, markerPath] = process.argv.slice(2);

if (!generatedDir || !markerPath) {
  console.error("Usage: node assign_generated_brunch_images.mjs <generatedDir> <markerPath>");
  process.exit(1);
}

if (!fs.existsSync(queuePath)) {
  console.error(`Missing queue: ${queuePath}`);
  process.exit(1);
}

if (!fs.existsSync(markerPath)) {
  console.error(`Missing marker: ${markerPath}`);
  process.exit(1);
}

const markerTime = fs.statSync(markerPath).mtimeMs;
const queue = JSON.parse(fs.readFileSync(queuePath, "utf8"))
  .filter((item) => !fs.existsSync(path.join(outRoot, item.image)));

const generated = fs.readdirSync(generatedDir)
  .filter((name) => name.endsWith(".png"))
  .map((name) => {
    const file = path.join(generatedDir, name);
    const stat = fs.statSync(file);
    return { file, mtime: stat.mtimeMs };
  })
  .filter((item) => item.mtime > markerTime)
  .sort((a, b) => a.mtime - b.mtime);

if (generated.length === 0) {
  console.error("No generated images found after marker.");
  process.exit(1);
}

if (generated.length > queue.length) {
  console.error(`Generated ${generated.length} images but only ${queue.length} queue slots remain.`);
  process.exit(1);
}

for (let index = 0; index < generated.length; index += 1) {
  const source = generated[index].file;
  const target = path.join(outRoot, queue[index].image);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(source, target);
  console.log(`${path.basename(source)} -> ${queue[index].image}`);
}

console.log(`assigned=${generated.length}`);
