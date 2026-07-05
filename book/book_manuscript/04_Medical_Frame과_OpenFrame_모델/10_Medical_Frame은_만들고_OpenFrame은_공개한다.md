# 10장. Medical Frame은 만들고, OpenFrame은 공개한다

공익을 오래 하려면 역할이 나뉘어야 한다.

모든 것을 한 회사 안에 넣으면 처음에는 단순해 보인다. 같은 팀이 만들고, 팔고, 공개하고, 무료 지원까지 하면 빠르게 움직일 수 있을 것 같다. 하지만 시간이 지나면 충돌이 생긴다.

수익을 내야 하는 일과 무료로 나누어야 하는 일이 같은 기준으로 움직이면 어느 한쪽이 흐려진다. 돈을 벌어야 할 영역까지 무료로 열면 회사가 지친다. 공개해야 할 영역까지 전부 닫으면 공익성이 사라진다. 지원 대상을 감정으로 정하면 불공정해지고, 유료 고객과 무료 사용자의 경계가 흐려지면 운영이 무너진다.

그래서 Medical Frame과 OpenFrame은 역할을 나누어야 한다.

Medical Frame은 만든다.

기술을 만들고, 제품을 만들고, 병원과 기업에 판매하고, 보안과 연동과 유지보수 책임을 진다. 좋은 사람을 고용하고, 개발 속도를 유지하고, 고객에게 약속한 수준의 지원을 제공한다. 병원 EMR connector, on-prem deployment, private inference, RBAC, audit log, SLA/support, 병원별 workflow customization 같은 영역은 Medical Frame의 유료 운영 영역이다.

이 영역은 돈을 받아야 한다.

돈을 받는 것이 부끄러운 일이 아니다. 책임이 붙는 영역에는 비용이 붙어야 한다. 병원 운영을 지원하려면 장애 대응, 문서, 교육, 보안 검토, 전산팀 협의, 개인정보 처리 원칙이 필요하다. 이것을 무료라고 말하는 것은 착한 것이 아니라 무책임할 수 있다.

OpenFrame은 공개한다.

OpenFrame은 기술과 지식을 공익적으로 열어두는 인프라다. core, demo, synthetic data, mock patient dataset, architecture docs, prompt templates, basic extractor, RAG pipeline, 설치 가이드, 교육자료를 공개한다. 학생, 초기 연구자, 작은 병원, 봉사단체, 공익기관이 시작할 수 있는 첫 계단을 만든다.

OpenFrame은 Medical Frame의 반대편이 아니다.

OpenFrame은 Medical Frame이 벌어온 돈과 기술을 사회로 돌려보내는 통로다. Medical Frame은 지속 가능성을 만들고, OpenFrame은 접근성을 만든다. Medical Frame이 없으면 OpenFrame은 유지될 돈이 부족하고, OpenFrame이 없으면 Medical Frame은 또 하나의 닫힌 기술 회사가 된다.

둘은 서로를 견제하고, 서로를 먹여 살려야 한다.

HyperFrame에서 이 구분은 더 선명해진다.

HyperFrame core는 공개할 수 있다. HyperClick demo도 공개할 수 있다. OpenEMR connector, synthetic data, prompt templates, architecture docs, basic RAG pipeline, basic HyperIRB extractor는 공개 가능한 범위에 있다. 공개하면 개발자와 연구자가 검증할 수 있고, 작은 기관이 시작할 수 있고, 병원도 제품의 방향을 더 투명하게 볼 수 있다.

하지만 병원별 운영은 공개 영역이 아니다.

실제 병원 EMR connector는 병원별 환경과 보안 정책에 묶인다. 실제 환자 데이터는 공개 대상이 아니다. credential, token, deploy key, 운영 서버, SSO, 접근권한, 감사 로그, 병원 내부 workflow는 계약과 승인 안에서만 다루어야 한다.

이 경계를 분명히 해야 한다.

공개 가능한 것을 닫아두면 신뢰가 생기지 않는다.

잠가야 할 것을 열어두면 안전이 무너진다.

Medical Frame과 OpenFrame의 역할 분리는 바로 이 균형을 위한 구조다.

Medical Frame은 돈 있는 곳에서 정당하게 번다. 병원, 기업, 대형기관, 해외 시장에서 운영 책임을 지고 비용을 받는다. 그 돈으로 사람을 고용하고, 제품을 유지하고, 공익사업을 지탱한다.

OpenFrame은 돈 없는 곳에 나눈다. 작은 병원, 봉사단체, 학생, 초기 연구자, 공익기관이 시작할 수 있도록 공개 도구와 교육자료와 제한된 지원을 제공한다.

이 구조는 공익과 수익의 충돌을 줄인다.

돈을 버는 일이 공익을 배신하지 않게 하고, 무료로 나누는 일이 회사의 지속 가능성을 무너뜨리지 않게 한다.

나는 Medical Frame이 돈을 버는 것을 숨기고 싶지 않다.

오히려 분명히 말해야 한다고 생각한다. 우리는 병원 운영과 보안과 연동과 지원에서 돈을 번다. 그리고 그 돈으로 OpenFrame을 통해 공개하고, 교육하고, 작은 기관에 설치하고, 연구자에게 도구를 연다.

공익은 돈을 모르는 척해서 오래가는 것이 아니다.

돈의 흐름을 정직하게 설계할 때 오래간다.

Core는 무료 공개.

병원 운영, 보안, 연동, 지원은 유료.

이 원칙이 Medical Frame과 OpenFrame을 함께 살리는 기본 문장이다.
