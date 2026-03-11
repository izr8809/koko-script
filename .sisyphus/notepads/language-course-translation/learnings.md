
## [2026-03-10] Task 15: 일본어 코스 재설계 — COMPLETED

### Result
- 파일: ~/a0/a0/ja.txt
- 라인 수: 1867줄
- 18스토리 완성
- 10회 검증 완료
- 주요 트랙 테마: PI(자기소개/일상), TR(여행/교통), KD(애니/드라마), KP(J-Pop/아이돌), CR(직장/비즈니스)

### Key Design Decisions
- 혈액형(血液型) 사용 — MBTI 대신 일본 문화에 맞게 (localization-guide.md 참고)
- LINE 사용 — 카카오톡 대신
- 渋谷/六本木/浅草 등 일본 지명 사용
- 焼肉/ラーメン/親子丼/カレーライス 등 일본 음식 사용
- YOASOBI/King Gnu 등 J-Pop 아티스트 사용
- 握手会(악수회) — 일본 아이돌 문화 특유의 팬 이벤트
- コミケ(코믹마켓) — 일본 오타쿠 문화 핵심 이벤트
- 花江夏樹/神谷浩史 등 실제 일본 성우 이름 사용

### Structural Fixes Applied During Verification
- TR-3 sim1: AI/User 역할 교체 (User가 길을 묻도록)
- TR-3 sim2/3: AI/User 역할 교체 (User가 티켓/플랫폼 묻도록)
- TR-4 sim2: AI/User 역할 교체 (User가 조식/Wi-Fi 묻도록)
- TR-4 sim3: AI/User 역할 교체 (User가 체크아웃 요청하도록)
- CR-2 sim2: AI/User 역할 교체 (User가 상사에게 지시 요청하도록)
- CR-2 sim3: AI/User 역할 교체 (User가 상사에게 보고하도록)
- PI-4 sim3: 연속 User 라인 제거, 4줄 구조로 정리
- TR-2: 親子丼 → カレーライス (매운 음식으로 교체, 현실성 확보)
- KP-3 sim2: User 2선택지 앞뒤 맥락 수정
- PI-2: 12턴 한글 → 12ターン 일본어로 수정

## [2026-03-10] Task 16: 영어 코스 재설계 — COMPLETED

- 파일: ~/a0/a0/en.txt, 2011줄
- 18스토리 완성, 10회 검증
- 트랙 테마: PI(First Meeting/Small Talk/Plans/Texting), TR(Coffee Shop/Restaurant/Directions/Hotel), KD(Netflix/Movies/Sports/Gaming), KP(Music Taste/Concert/Fan Culture), CR(Introductions/Meetings/Emails)
- 미국 문화 요소: iMessage, SoHo/Central Park/Times Square/Brooklyn, BBQ/burger/pizza, Taylor Swift/Beyoncé, NBA/NFL, Starbucks
- 한국 문화 요소 0건 확인
- User 2선택지 맥락 불일치 3건 수정 (KD-2 Set4 이중 User 라인, KP-1 Set5 AI 응답, CR-3 Set5 AI 응답)
- 레지스터: PI/KD casual, TR polite, KP mixed, CR formal — 일관성 유지
