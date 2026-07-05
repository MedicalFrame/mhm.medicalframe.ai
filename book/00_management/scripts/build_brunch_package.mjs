import fs from "node:fs";
import path from "node:path";

const root = path.resolve(new URL("../../", import.meta.url).pathname);
const sourceRoot = path.join(root, "book_manuscript");
const outRoot = path.join(root, "brunch");
const postsRoot = path.join(outRoot, "posts");
const assetRoot = path.join(outRoot, "assets", "illustrations");

const chapters = [
  ["00", "00_frontmatter/00_프롤로그_방지송이_대체_뭔데_씹덕아.md", "프롤로그"],
  ["01", "01_기업은_사회_밖에서_살_수_없다/01_기업은_혼자_돈을_벌지_않는다.md", "1부"],
  ["02", "01_기업은_사회_밖에서_살_수_없다/02_사회기업윤리란_무엇인가.md", "1부"],
  ["03", "01_기업은_사회_밖에서_살_수_없다/03_탐욕은_성장_전략이_아니다.md", "1부"],
  ["04", "02_나는_딴돈의_절반만_가져가/04_절반만_가져간다는_것.md", "2부"],
  ["05", "02_나는_딴돈의_절반만_가져가/05_돈_있는_곳에서_벌고_돈_없는_곳에는_나눈다.md", "2부"],
  ["06", "02_나는_딴돈의_절반만_가져가/06_공짜는_돈_없이_유지되지_않는다.md", "2부"],
  ["07", "03_의료_교육_연구는_모두의_것이다/07_의료는_상품이기_전에_생존_조건이다.md", "3부"],
  ["08", "03_의료_교육_연구는_모두의_것이다/08_교육은_잠기면_계급이_된다.md", "3부"],
  ["09", "03_의료_교육_연구는_모두의_것이다/09_연구는_닫힌_성이_아니라_열린_기반이다.md", "3부"],
  ["10", "04_Medical_Frame과_OpenFrame_모델/10_Medical_Frame은_만들고_OpenFrame은_공개한다.md", "4부"],
  ["11", "04_Medical_Frame과_OpenFrame_모델/11_지송재단과_OpenFrame.md", "4부"],
  ["12", "04_Medical_Frame과_OpenFrame_모델/12_지원은_감정이_아니라_기준으로_한다.md", "4부"],
  ["13", "05_AI_EMR_선언/13_AI_EMR은_왜_열려_있어야_하는가.md", "5부"],
  ["14", "05_AI_EMR_선언/14_기존_EMR을_갈아엎기_전에_옆에_켠다.md", "5부"],
  ["15", "05_AI_EMR_선언/15_작은_병원부터_좋은_시스템을_쓴다.md", "5부"],
  ["16", "06_무료_배포는_마케팅이_아니라_실증이다/16_봉사단체에서_시작하는_이유.md", "6부"],
  ["17", "06_무료_배포는_마케팅이_아니라_실증이다/17_공익_배포에도_안전장치가_필요하다.md", "6부"],
  ["18", "06_무료_배포는_마케팅이_아니라_실증이다/18_실증이_끝나면_표준이_된다.md", "6부"],
  ["19", "07_방해와_저항을_다루는_법/19_나를_방해하는_사람들은_언제나_있다.md", "7부"],
  ["20", "07_방해와_저항을_다루는_법/20_나는_딴_돈의_절반만_가져가.md", "7부"],
  ["21", "07_방해와_저항을_다루는_법/21_적을_만들지_말고_구조를_바꿔라.md", "7부"],
  ["22", "07_방해와_저항을_다루는_법/22_선언보다_설치.md", "7부"],
  ["23", "08_절반만_가져가는_회사의_운영_원칙/23_가격_정책도_윤리다.md", "8부"],
  ["24", "08_절반만_가져가는_회사의_운영_원칙/24_사람에게_몫을_남긴다.md", "8부"],
  ["25", "08_절반만_가져가는_회사의_운영_원칙/25_사회로_다시_흘려보낸다.md", "8부"],
  ["26", "09_새로운_기업윤리_선언/26_기업은_공익을_외주_줄_수_없다.md", "9부"],
  ["27", "09_새로운_기업윤리_선언/27_오픈소스는_사회적_약속이다.md", "9부"],
  ["28", "09_새로운_기업윤리_선언/28_사회기업윤리_선언.md", "9부"],
  ["99", "00_frontmatter/99_에필로그_의료는_모두의_것이다.md", "에필로그"],
];

const existingHeroImages = {
  "01": "../illustrations/01-company-infrastructure.png",
  "02": "../illustrations/02-social-enterprise-os.png",
  "03": "../illustrations/03-greed-vs-ecosystem.png",
  "04": "../illustrations/04-half-principle.png",
  "05": "../illustrations/05-differential-pricing.png",
};

const visualAngles = [
  "핵심 개념을 한눈에 보여주는 대표 장면",
  "운영 구조와 이해관계 흐름을 보여주는 중간 장면",
  "독자가 기억할 결론을 상징하는 마무리 장면",
];

const sceneVariants = [
  "a transparent infrastructure hub with connected public-service modules",
  "a circular stakeholder table balancing revenue, care, safety, and access",
  "an open clinic-and-lab bridge where knowledge flows from experts to communities",
  "a maintenance workshop for medical software with tools, checklists, and care symbols",
  "a pathway from a small local clinic to a shared national-scale platform",
  "a modular library of open medical components being assembled into a living system",
  "a quiet conflict-resolution scene where structure redirects pressure into cooperation",
  "a foundation-like support network distributing resources by clear criteria",
  "a safety cockpit for AI-assisted medicine with human oversight at the center",
  "a public commons garden where medical data, education, and tools are tended carefully",
];

const representationAccents = [
  "include an intergenerational team with a wheelchair user and a young clinician",
  "include women in technical and clinical roles, one older adult, and varied body types",
  "include a patient advocate, educator, engineer, clinician, and nonprofit operator with varied skin tones",
  "include one cane user, one seated participant, and collaborators with varied gender presentation",
  "include a rural-clinic worker, software maintainer, caregiver, and medical trainee",
  "include people with different professional clothing and natural non-identical silhouettes",
  "include a calm group where no single supporting demographic dominates the scene",
  "include collaborators at different heights, ages, and roles around the central woman protagonist",
];

const cameraVariants = [
  "slight top-down isometric view with the protagonist near the center",
  "wide isometric overview with several small connected platforms",
  "closer editorial isometric framing around a roundtable decision scene",
  "diagonal isometric composition with a clear foreground object and airy background",
  "symmetrical isometric composition with balanced modules around the protagonist",
  "off-center isometric composition with generous negative space and a visible workflow path",
];

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function readChapter(file) {
  const raw = fs.readFileSync(path.join(sourceRoot, file), "utf8").trim();
  const lines = raw.split(/\r?\n/);
  const firstHeading = lines.find((line) => line.startsWith("# "));
  const title = (firstHeading || path.basename(file, ".md"))
    .replace(/^#\s*/, "")
    .replace(/^\d+장\.\s*/, "")
    .replace(/^에필로그\.\s*/, "에필로그. ")
    .trim();
  const body = lines.filter((line) => line !== firstHeading).join("\n").trim();
  return { title, body };
}

function makePostName(id, title) {
  const safe = title.replace(/[\\/:*?"<>|]/g, "").replace(/\s+/g, "_");
  return `${id}_${safe}.md`;
}

function splitParagraphs(body) {
  return body.split(/\n{2,}/).map((part) => part.trim()).filter(Boolean);
}

function imageBlock(id, slot, title) {
  const rel = `../assets/illustrations/${id}/${String(slot).padStart(2, "0")}.png`;
  return `![${title} 삽화 ${slot}](${rel})\n\n_${title} - 삽화 ${slot}_`;
}

function pickVariant(list, id, slot) {
  const numericId = id === "99" ? 29 : Number.parseInt(id, 10);
  return list[((Number.isNaN(numericId) ? 0 : numericId) * 3 + slot - 1) % list.length];
}

function buildPost({ id, part, source, title, body }) {
  const paragraphs = splitParagraphs(body);
  const firstCut = Math.max(1, Math.ceil(paragraphs.length / 3));
  const secondCut = Math.max(firstCut + 1, Math.ceil((paragraphs.length * 2) / 3));
  const out = [];

  out.push(`# ${title}`);
  out.push(`> 출처: ${part} · ${source}`);
  out.push(imageBlock(id, 1, title));

  paragraphs.forEach((paragraph, index) => {
    if (index === firstCut) out.push(imageBlock(id, 2, title));
    if (index === secondCut) out.push(imageBlock(id, 3, title));
    out.push(paragraph);
  });

  return `${out.join("\n\n")}\n`;
}

function makePrompt({ id, part, source, title, slot }) {
  const angle = visualAngles[slot - 1];
  return [
    `Use case: productivity-visual`,
    `Asset type: Brunch article illustration for the MHMbook chapter "${title}"`,
    `Primary request: Create a polished 3D isometric editorial illustration for a Korean essay titled "${title}".`,
    `Concept angle: ${angle}.`,
    `Book context: "나는 딴 돈의 절반만 가져가" is about MedicalFrame, social enterprise ethics, public-interest infrastructure, open access, sustainable pricing, medical AI safety, and maintenance responsibility.`,
    `Chapter context: ${part}, source file ${source}.`,
    `Scene/backdrop: clean white studio background with soft pale-blue medical-tech glow.`,
    `Scene variant: ${pickVariant(sceneVariants, id, slot)}.`,
    `Representation accent: ${pickVariant(representationAccents, id, slot)}.`,
    `People and representation: use a recurring adult woman protagonist/founder/operator whenever a central human figure appears. Do not make the central protagonist male. Supporting people must be visibly diverse across gender presentation, age, professional role, body type, skin tone, and accessibility needs while staying respectful and natural.`,
    `Visual variety: avoid repeating the same composition across chapters. Vary the main metaphor, camera angle, object layout, number of people, and representation mix so the full article set feels diverse rather than template-generated.`,
    `Composition: wide horizontal 2:1 image, ${pickVariant(cameraVariants, id, slot)}, centered and airy, suitable as a Brunch article image. Use visual symbols and narrative objects, not text.`,
    `Style: premium 3D isometric render, white and light blue palette, restrained warm gold accents, translucent glass panels, soft shadows, calm trustworthy editorial finish.`,
    `Avoid: readable text, labels, logos, brand marks, national flags, political symbols, dark dystopian mood, clutter, stock-photo realism, cartoon style, scary imagery.`,
  ].join("\n");
}

ensureDir(postsRoot);
ensureDir(assetRoot);

const rows = [];
const promptRows = [];

for (const [id, source, part] of chapters) {
  const { title, body } = readChapter(source);
  const chapterAssetDir = path.join(assetRoot, id);
  ensureDir(chapterAssetDir);

  const postPath = path.join(postsRoot, makePostName(id, title));
  fs.writeFileSync(postPath, buildPost({ id, part, source, title, body }), "utf8");

  if (existingHeroImages[id]) {
    const existingPath = path.join(assetRoot, existingHeroImages[id]);
    const firstSlot = path.join(chapterAssetDir, "01.png");
    if (fs.existsSync(existingPath) && !fs.existsSync(firstSlot)) {
      fs.copyFileSync(existingPath, firstSlot);
    }
  }

  for (let slot = 1; slot <= 3; slot += 1) {
    const imagePath = path.join(chapterAssetDir, `${String(slot).padStart(2, "0")}.png`);
    const relImagePath = path.relative(outRoot, imagePath);
    const exists = fs.existsSync(imagePath);
    rows.push({ id, title, part, source, slot, image: relImagePath, status: exists ? "done" : "missing" });
    promptRows.push({ id, title, part, source, slot, image: relImagePath, prompt: makePrompt({ id, part, source, title, slot }) });
  }
}

const manifest = [
  "# MHMbook 브런치 전체 산출 매니페스트",
  "",
  `생성일: ${new Date().toISOString().slice(0, 10)}`,
  "",
  "## 산출 현황",
  "",
  "| 글 ID | 제목 | 구분 | 삽화 | 상태 | 경로 |",
  "|---|---|---|---:|---|---|",
  ...rows.map((row) => `| ${row.id} | ${row.title} | ${row.part} | ${row.slot} | ${row.status} | \`${row.image}\` |`),
  "",
  "## 삽화 생성 프롬프트",
  "",
  ...promptRows.map((row) => [
    `### ${row.id}-${row.slot}. ${row.title}`,
    "",
    `대상 파일: \`${row.image}\``,
    "",
    "```text",
    row.prompt,
    "```",
    "",
  ].join("\n")),
].join("\n");

fs.writeFileSync(path.join(outRoot, "manifest.md"), manifest, "utf8");
fs.writeFileSync(
  path.join(outRoot, "image_queue.json"),
  `${JSON.stringify(promptRows.filter((row) => !fs.existsSync(path.join(outRoot, row.image))), null, 2)}\n`,
  "utf8",
);

const summary = rows.reduce((acc, row) => {
  acc.total += 1;
  if (row.status === "done") acc.done += 1;
  return acc;
}, { total: 0, done: 0 });

console.log(`posts=${chapters.length}`);
console.log(`images=${summary.done}/${summary.total}`);
console.log(`out=${outRoot}`);
