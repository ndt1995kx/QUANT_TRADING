# 02 — Các kênh học thuật về quant trading

> Cập nhật: 2026-10-01 · Tài liệu giáo dục, **không phải tư vấn đầu tư** và không phải quảng cáo cho bất kỳ khóa học hay sản phẩm nào.

## 0. Cách đọc tài liệu này

**Nhãn đối chiếu** (cột "Đối chiếu"):

| Nhãn | Nghĩa |
|---|---|
| ✔ | Đã đối chiếu (tra cứu 10/2026): nội dung khớp với kết quả tìm kiếm trỏ tới trang chính thức |
| ? | Chưa đối chiếu được — dựa trên kiến thức chung hoặc dữ kiện không đủ chắc chắn |
| ✖ | Có dấu hiệu đã ngừng hoạt động |

**Giới hạn của lần tra cứu này — hãy đọc trước khi dựa vào số liệu:**

- Môi trường soạn thảo **không mở trực tiếp được trang gốc** (truy cập web bị chặn theo chính sách mạng) và hạn mức tìm kiếm bị cạn giữa chừng. Mọi nhãn ✔ nghĩa là *đã khớp với nội dung trang chính thức hiển thị trong kết quả tìm kiếm*, không phải *đã mở và đọc trang*.
- **Giá, lịch thi, hạn nộp hồ sơ, ngày hội nghị** thay đổi thường xuyên. Chúng được ghi để tham khảo; luôn kiểm tra lại trên liên kết chính thức.
- Phần **Việt Nam** (mục 11) gần như **chưa được kiểm chứng**, và các mục **7–10** (sách, thư viện, cộng đồng, dữ liệu) chủ yếu là kiến thức chung mang nhãn `?`.

## 1. Bản đồ nhanh

| Nhóm kênh | Dùng để | Chi phí điển hình | Mục |
|---|---|---|---|
| Preprint và tạp chí | Đọc nghiên cứu gốc, mới nhất | Preprint miễn phí; tạp chí thường thuê bao | [2](#2-nghiên-cứu-và-bài-báo) |
| Hội nghị | Gặp nhà nghiên cứu và practitioner, nắm xu hướng | Phí đăng ký | [3](#3-hội-nghị-và-sự-kiện) |
| Thạc sĩ | Nền tảng sâu, bằng cấp | Cao (trừ chương trình miễn học phí) | [4](#4-chương-trình-thạc-sĩ) |
| Chứng chỉ nghề nghiệp | Chuẩn hóa kiến thức, tín hiệu nghề nghiệp | Trung bình – cao | [5](#5-chứng-chỉ-nghề-nghiệp) |
| Khóa học / bài giảng mở | Tự học nền tảng | Miễn phí – thấp | [6](#6-khóa-học-và-bài-giảng-mở) |
| Sách và bài báo kinh điển | Chiều sâu có hệ thống | Thấp | [7](#7-sách-và-bài-báo-kinh-điển) |
| Nền tảng, thư viện, cuộc thi | Làm thật, thử nghiệm | Miễn phí – trung bình | [8](#8-nền-tảng-thực-hành-thư-viện-mã-nguồn-mở-và-cuộc-thi) |
| Cộng đồng, blog, podcast | Cập nhật, hỏi đáp | Miễn phí | [9](#9-cộng-đồng-blog-và-podcast) |
| Dữ liệu để học | Thực hành với dữ liệu thật | Miễn phí – thấp | [10](#10-nguồn-dữ-liệu-để-học) |
| Việt Nam | Bối cảnh trong nước | — | [11](#11-tại-việt-nam) |
| Lộ trình học và cách đánh giá nguồn | Định hướng, tránh bẫy | — | [12](#12-lộ-trình-học-gợi-ý-theo-giai-đoạn-không-theo-thời-gian), [13](#13-cách-đánh-giá-một-nguồn-học-hoặc-sản-phẩm-quant) |

## 2. Nghiên cứu và bài báo

### 2.1 Kho preprint và working paper

| Kênh | Nội dung | Chi phí / mức mở | Đối chiếu |
|---|---|---|---|
| [arXiv q-fin](https://arxiv.org/archive/q-fin) | Preprint tài chính định lượng, chia 9 mục con (bảng dưới) | Miễn phí | ✔ |
| [SSRN — Financial Economics Network](https://www.ssrn.com/index.cfm/en/fen/) | Preprint, working paper, luận án, tài liệu giảng dạy tài chính | Kho preprint mở | ✔ |
| [NBER Working Papers](https://www.nber.org/papers) | Working paper kinh tế/tài chính | 3 lượt tải miễn phí mỗi năm; miễn phí đầy đủ cho cư dân nước có GDP/người dưới 35,000 USD (theo danh sách IMF 2017), công chức Mỹ, báo chí — [điều kiện](https://www.nber.org/subscribe/free-working-paper-access). Việt Nam có thuộc diện này hay không: **chưa xác minh** | ✔ |
| RePEc / IDEAS (`ideas.repec.org`) | Thư mục mở bài báo và working paper kinh tế – tài chính | Miễn phí | ? |

**Các mục con của arXiv q-fin** (phân loại chính thức; hay bị quên mục q-fin.PR):

| Mục | Phạm vi |
|---|---|
| **q-fin.TR** — Trading and Market Microstructure | Vi cấu trúc, thanh khoản, thiết kế sàn/đấu giá, giao dịch tự động, mô hình agent-based, market making |
| **q-fin.PM** — Portfolio Management | Chọn và tối ưu chứng khoán, phân bổ vốn, chiến lược, đo hiệu suất |
| **q-fin.ST** — Statistical Finance | Thống kê, kinh tế lượng, econophysics cho dữ liệu thị trường |
| **q-fin.CP** — Computational Finance | Monte Carlo, PDE, lattice, phương pháp số cho mô hình tài chính |
| **q-fin.RM** — Risk Management | Đo lường và quản trị rủi ro trong giao dịch, ngân hàng, bảo hiểm, doanh nghiệp |
| **q-fin.PR** — Pricing of Securities | Định giá và phòng hộ chứng khoán, phái sinh, sản phẩm cấu trúc |
| **q-fin.MF** — Mathematical Finance | Giải tích ngẫu nhiên, xác suất, giải tích hàm, đại số, hình học cho tài chính |
| **q-fin.GN** — General Finance | Phương pháp định lượng tổng quát ứng dụng cho tài chính |
| **q-fin.EC** — Economics | Bí danh của econ.GN: kinh tế vi mô/vĩ mô và các chủ đề kinh tế ngoài tài chính |

### 2.2 Tạp chí bình duyệt

Còn phát hành tính đến 2025–2026 theo trang chính thức. Quyền truy cập khác nhau giữa các tạp chí; nhiều bài có bản preprint miễn phí trên SSRN/arXiv — hãy kiểm tra trên trang tạp chí.

| Tạp chí | Nhà xuất bản | Phạm vi | Đối chiếu |
|---|---|---|---|
| [Journal of Finance](https://afajof.org/issue/volume-81-issue-3/) | AFA / Wiley | Mọi lĩnh vực tài chính (Vol. 81, 2026) | ✔ |
| [Journal of Financial Economics](https://www.sciencedirect.com/journal/journal-of-financial-economics) | Elsevier | Tài chính lý thuyết và thực nghiệm (Vol. 176–177, 2026) | ✔ |
| [Review of Financial Studies](https://academic.oup.com/rfs/issue/39/4) | Oxford UP / SFS | Financial economics (Vol. 39, 2026) | ✔ |
| [Quantitative Finance](https://www.tandfonline.com/toc/rquf20/current) | Taylor & Francis | Định giá phái sinh, vi cấu trúc, danh mục, mô hình agent-based (Vol. 26, 2026) | ✔ |
| [Journal of Portfolio Management](https://www.pm-research.com/content/iijpormgmt) | PM-Research | Quản lý danh mục, thực hành đầu tư (Vol. 52, 2026) | ✔ |
| [Journal of Financial Data Science](https://www.pm-research.com/content/iijjfds) | PM-Research | AI, ML và dữ liệu trong đầu tư (Vol. 8, 2026); thuê bao | ✔ |
| [Mathematical Finance](https://onlinelibrary.wiley.com/toc/14679965/2026/36/2) | Wiley | Toán và thống kê cho bài toán tài chính (Vol. 36, 2026) | ✔ |
| [Finance and Stochastics](https://link.springer.com/journal/780/volumes-and-issues) | Springer | Mô hình ngẫu nhiên cho tài chính và bảo hiểm (Vol. 30, 2026) | ✔ |
| [SIAM Journal on Financial Mathematics](https://www.siam.org/publications/siam-journals/siam-journal-on-financial-mathematics/) | SIAM | Toán tài chính (Vol. 17, 2026) | ✔ |
| [Journal of Computational Finance](https://www.risk.net/journal-of-computational-finance) | Risk.net | Tài chính tính toán (Vol. 29, 2025–2026) | ✔ |
| [Journal of Investment Strategies](https://www.risk.net/journal-of-investment-strategies) | Risk.net | Chiến lược đầu tư, thuật toán (thấy số 2025; chưa thấy số 2026) | ✔ |
| Journal of Financial Markets | Elsevier | Giao dịch, định giá chứng khoán, vi cấu trúc (thấy bài 2025) | ✔ |
| [Financial Analysts Journal](https://www.tandfonline.com/journals/ufaj20) | CFA Institute / Taylor & Francis | Đầu tư thực hành (Vol. 82, 2026) | ✔ |

**Cần kiểm tra lại trước khi trích làm "nguồn hiện hành":**

- *Journal of Trading* (PM-Research): trong kết quả tra cứu, trang chính thức chỉ liệt kê số đến Fall 2018 — trạng thái hiện nay **chưa chắc chắn** (?).
- *Market Microstructure and Liquidity* (World Scientific): kết quả cho thấy số cuối là năm 2020 — có dấu hiệu đã ngừng (✖).
- Để tìm nghiên cứu về vi cấu trúc và thực thi hiện nay, nên bắt đầu từ *Quantitative Finance*, *Journal of Financial Markets* và arXiv q-fin.TR.

## 3. Hội nghị và sự kiện

Phí đăng ký của các sự kiện dưới đây **chưa được đối chiếu**.

| Sự kiện | Tổ chức | Kỳ gần nhất / kỳ tới | Đối chiếu |
|---|---|---|---|
| [QuantMinds International](https://informaconnect.com/quantminds-international/) | Informa Connect | Tới: 16–19/11/2026, London | ✔ |
| [Bachelier Finance Society World Congress](https://www.bachelierfinance.org/bfs-congresses) | Bachelier Finance Society | Lần 13: 29/6–3/7/2026, Bologna. Lần 14: 17–21/7/2028, Stellenbosch (Nam Phi) | ✔ |
| [ACM ICAIF](https://icaif2026.org/) (AI in Finance) | ACM | Lần 7: 14–17/11/2026, Đại học Bocconi, Milan | ✔ |
| [SIAM Financial Mathematics & Engineering](https://www.siam.org/conferences-events/siam-conferences/fm27/) | SIAM | Gần nhất FM25: 15–18/7/2025, Miami. FM27: có trang chính thức, ngày/địa điểm chưa rõ | ✔ |
| [AFA Annual Meeting](https://afajof.org/annual-meeting/) | American Finance Association | Tới: 3–5/1/2027, Washington D.C. | ✔ |
| [WFA Annual Meeting](https://westernfinance.org/conference-2026/) | Western Finance Association | Gần nhất: 21–24/6/2026, Denver | ✔ |
| [EFA Annual Meeting](https://efa2026.efa-finance.org/program/) | European Finance Association | Lần 53: 19–22/8/2026, Ghent (Bỉ) | ✔ |
| [Computing in Economics and Finance (CEF)](https://comp-econ.com/32nd-cef-conference/) | Society for Computational Economics | Lần 32: 29/6–1/7/2026, Venice | ✔ |
| [Workshop "Advances in Financial AI"](https://sites.google.com/view/iclr2026finai/home) tại ICLR 2026 | ICLR | 27/4/2026, Rio de Janeiro (lần thứ 2) | ✔ |
| Workshop AI-in-finance tại ICML / NeurIPS 2026 | ICML, NeurIPS | Không thấy workshop tài chính chuyên biệt trong kết quả (không có nghĩa là không có) | ? |

## 4. Chương trình thạc sĩ

Danh sách **không phải xếp hạng**; các chương trình có thể thay đổi nội dung, hồ sơ và học phí theo từng khóa.

| Chương trình | Trường | Mô tả ngắn | Đối chiếu |
|---|---|---|---|
| [MFE](https://mfe.baruch.cuny.edu/) | Baruch College (CUNY) | 12 môn × 3 tín chỉ; toàn thời gian 3 học kỳ (bán thời gian 5–6) | ✔ |
| [MSCF — Computational Finance](https://www.cmu.edu/mscf/academics/index.html) | Carnegie Mellon | Toàn thời gian, Pittsburgh và New York | ✔ |
| [MS Financial Engineering](https://ieor.columbia.edu/financial-engineering-msfe) | Columbia Engineering (IEOR) | 1 năm, 36 điểm, nhiều hướng chuyên sâu | ✔ |
| [MS in **Mathematics in Finance**](https://math-finance.cims.nyu.edu/academics/) | NYU Courant | Toàn thời gian 3 học kỳ / bán thời gian / song bằng MBA với Stern. *Lưu ý tên đúng — không phải "Mathematical Finance"* | ✔ |
| [Master in Finance (MFin)](https://bcf.princeton.edu/academic-programs/master-in-finance/) | Princeton (Bendheim Center) | 2 năm | ✔ |
| [MFE](https://mfe.haas.berkeley.edu/) | UC Berkeley Haas | 1 năm toàn thời gian hoặc 2 năm Flex | ✔ |
| [MS in Financial Mathematics](https://finmath.uchicago.edu/curriculum/) | University of Chicago | Trực tiếp (~15 tháng) hoặc Online; hướng Financial Computing, ML & AI, Options, Rates & Credit, Trading | ✔ |
| [MSc Mathematics and Finance](https://www.imperial.ac.uk/study/courses/postgraduate-taught/mathematics-finance/) | Imperial College London | 1 năm toàn thời gian | ✔ |
| [MSc Mathematical and Computational Finance](https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-computational-finance) | Oxford | 10 tháng | ✔ |
| [MSc Quantitative Finance](https://www.msfinance.uzh.ch/en.html) | UZH + ETH Zürich | Bằng liên kết, tiếng Anh, 90 ECTS | ✔ |
| [MSc Quantitative Finance](https://www.math.nus.edu.sg/pg/mqf/) | NUS (Toán, phối hợp Kinh tế & Thống kê) | 40 tín chỉ, 1–2 năm | ✔ |
| [MSc Financial Engineering](https://www.wqu.edu/mscfe) | WorldQuant University | 100% online (chi tiết dưới) | ✔ |

**WorldQuant University MScFE** (đã đối chiếu qua [trang tuyển sinh](https://www.wqu.edu/mscfe-apply) và [FAQ](https://www.wqu.edu/faq)): học phí 0, không phí nộp hồ sơ, không phí cấp bằng; 100% online, 2 năm (9 môn + capstone); kiểm định DEAC (Mỹ); đầu vào yêu cầu bằng cử nhân và bài *Quantitative Proficiency Test* (≥ 75%, 60 câu, 2 giờ, tối đa 2 lần). Kỳ nhập học 10/2026 đã hết hạn nộp (29/9/2026); kỳ sau chưa rõ. **Chưa xác minh:** việc Việt Nam có công nhận văn bằng online loại này hay không, và chi phí ngoài (bản sao bảng điểm, chứng minh tiếng Anh).

## 5. Chứng chỉ nghề nghiệp

Giá lấy từ trang chính thức tại thời điểm tra cứu (10/2026), tính bằng ngoại tệ và **thay đổi thường xuyên**; một số khoản đã quá hạn đăng ký. CQF và EPAT là chương trình đào tạo thương mại chứ không phải bằng đại học.

| Chứng chỉ | Đơn vị | Hình thức | Phí tham khảo | Đối chiếu |
|---|---|---|---|---|
| [CQF](https://www.cqf.com/about-cqf/program-fees/fees) | CQF | Online bán thời gian, ~6 tháng, 2 cấp; có thi cuối khóa | 18,595–19,695 EUR (khóa 01/2027, chưa gồm VAT) | ✔ |
| [FRM](https://www.garp.org/frm/fees-payments) | GARP | 2 bài thi trắc nghiệm trên máy; cần ≥ 2 năm kinh nghiệm quản trị rủi ro toàn thời gian | 800 USD/phần + 400 USD ghi danh một lần | ✔ |
| [CFA](https://www.cfainstitute.org/programs/cfa-program/dates-fees) | CFA Institute | 3 cấp, thi máy; hơn 300 giờ học mỗi cấp | Level I khoảng 1,140–1,490 USD cho kỳ 2026 (theo thông báo trước đó; cần xác nhận lại trên trang) | ✔ |
| [PRM](https://prmia.org/Public/Public/PRM/PricingAndSchedule.aspx) | PRMIA | 4 bài thi, hoàn tất trong 3 năm | 1,280 USD (không thành viên) + 150 USD phí hồ sơ | ✔ |
| [CAIA](https://caia.org/registration-and-fees/) | CAIA Association | 2 cấp, thi 2 lần/năm | 400 USD ghi danh + 995–1,395 USD/cấp | ✔ |
| [EPAT](https://www.quantinsti.com/epat) | QuantInsti | Online 6 tháng, có thi chứng nhận. "Accredited by CPD UK" là chứng nhận phát triển nghề nghiệp, **không phải** kiểm định học thuật | 9,499 USD (giá niêm yết, có thể đổi) | ✔ |

## 6. Khóa học và bài giảng mở

| Khóa | Tổ chức | Nội dung | Chi phí / mở | Đối chiếu |
|---|---|---|---|---|
| [18.642 Topics in Mathematics with Applications in Finance](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/syllabus/) (bản cập nhật của [18.S096](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)) | MIT OpenCourseWare | Đại số tuyến tính, xác suất, thống kê, quá trình ngẫu nhiên và ứng dụng tài chính; có video, ghi chú, bài tập | Miễn phí | ✔ |
| [15.450 Analytics of Finance](https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/) (2010 — tài liệu cũ) | MIT OCW (Sloan) | Itô, định giá, tối ưu động, Monte Carlo, kinh tế lượng tài chính | Miễn phí | ✔ |
| [Financial Engineering and Risk Management](https://www.coursera.org/specializations/financialengineering) | Columbia / Coursera | Định giá phái sinh, phân bổ tài sản, tối ưu danh mục | Chứng chỉ trả phí; quyền học thử miễn phí hiện nay chưa xác minh | ✔ |
| [CS 7646 Machine Learning for Trading](https://omscs.gatech.edu/cs-7646-machine-learning-trading) ([trang công khai](https://lucylabs.gatech.edu/ml4t/)) | Georgia Tech | Python cho dữ liệu tài chính, ML (hồi quy, Q-learning, KNN, cây) | Khóa OMSCS trả phí; tài liệu công khai đến Fall 2023; "miễn phí trên Udacity" chưa xác minh còn mở | ✔ |
| [Machine Learning and Reinforcement Learning in Finance](https://www.coursera.org/specializations/machine-learning-reinforcement-finance) | NYU Tandon / Coursera | ML và học tăng cường cho thị trường tài chính | Trả phí (có hỗ trợ tài chính) | ✔ |
| [Investment Management with Python and Machine Learning](https://www.coursera.org/specializations/investment-management-python-machine-learning) | EDHEC / Coursera | Python, xây danh mục, ML cho quản lý tài sản | Chưa rõ | ✔ |
| [Financial Markets](https://www.coursera.org/learn/financial-markets-global) (R. Shiller) và [bản Open Yale Courses](https://oyc.yale.edu/economics/econ-252) | Yale | Thị trường, rủi ro, tài chính hành vi (nền tảng, không phải quant sâu) | Học miễn phí; chứng chỉ Coursera trả phí | ✔ |

## 7. Sách và bài báo kinh điển

Tên sách, tác giả và năm xuất bản dưới đây là kiến thức chung về các tài liệu nền tảng; **chưa đối chiếu trực tuyến** (nhãn `?`). Hãy kiểm tra lần xuất bản mới nhất trước khi mua.

| Tác giả | Tên | Mức | Đáng đọc vì |
|---|---|---|---|
| Ernest P. Chan | *Quantitative Trading* (bản 2, 2021) | Nhập môn | Dựng quy trình quant ở quy mô cá nhân từ đầu |
| Rishi Narang | *Inside the Black Box* | Nhập môn | Cấu trúc một hệ quant: alpha, rủi ro, chi phí, danh mục, thực thi |
| Ernest P. Chan | *Algorithmic Trading* (2013), *Machine Trading* (2017) | Trung cấp | Các chiến lược cụ thể (mean reversion, momentum) kèm lý do chúng tồn tại |
| Lasse H. Pedersen | *Efficiently Inefficient* (2015) | Trung cấp | Các chiến lược của quỹ phòng hộ và nguồn lợi nhuận của chúng |
| Larry Harris | *Trading and Exchanges* (2003) | Trung cấp | Vi cấu trúc thị trường dành cho người làm thực tế |
| Stefan Jansen | *Machine Learning for Algorithmic Trading* (bản 2, 2020) | Trung cấp | ML áp dụng vào giao dịch, kèm mã |
| John C. Hull | *Options, Futures, and Other Derivatives* | Trung cấp | Nền tảng phái sinh |
| Marcos López de Prado | *Advances in Financial Machine Learning* (2018) | Nâng cao | Backtest và ML đúng cách: purged CV, chống overfitting |
| Marcos López de Prado | *Machine Learning for Asset Managers* (2020) | Nâng cao | ML cho xây dựng danh mục |
| Grinold & Kahn | *Active Portfolio Management* | Nâng cao | Khung lý thuyết về IC, breadth và information ratio |
| Roman Isichenko | *Quantitative Portfolio Management* (2021) | Nâng cao | Quản trị danh mục định lượng từ góc nhìn người làm thực tế |
| Cartea, Jaimungal & Penalva | *Algorithmic and High-Frequency Trading* (2015) | Nâng cao | Thực thi tối ưu, market making |
| Bouchaud, Bonart, Donier & Gould | *Trades, Quotes and Prices* (bản 2, 2018) | Nâng cao | Vi cấu trúc thị trường và tác động giá |
| Steven Shreve | *Stochastic Calculus for Finance* (I, II) | Nâng cao | Toán nền tảng cho định giá phái sinh |
| Kakushadze & Serur | *151 Trading Strategies* (2018) | Tham khảo | Danh mục chiến lược kèm công thức (bản trên SSRN) |
| Andrew Lo | *Adaptive Markets* (2017) | Đọc thêm | Khung "thị trường thích nghi" thay cho thị trường hiệu quả |
| Emanuel Derman | *My Life as a Quant* (2004) | Đọc thêm | Nghề quant từ bên trong |
| Gregory Zuckerman | *The Man Who Solved the Market* (2019) | Đọc thêm | Câu chuyện Renaissance Technologies (không phải sách kỹ thuật) |

**Bài báo nên đọc** (về kiểm định chiến lược):

| Bài | Nội dung |
|---|---|
| Bailey & López de Prado (2014), *The Deflated Sharpe Ratio* | Điều chỉnh Sharpe theo số lần thử và độ lệch/độ nhọn |
| Bailey, Borwein, López de Prado & Zhu, *The Probability of Backtest Overfitting* | Ước lượng xác suất chiến lược tốt nhất trong mẫu lại kém ngoài mẫu |
| Harvey, Liu & Zhu (2016), *…and the Cross-Section of Expected Returns* | Vì sao cần ngưỡng thống kê cao hơn khi đã có hàng trăm nhân tố được thử |

## 8. Nền tảng thực hành, thư viện mã nguồn mở và cuộc thi

Mọi mục dưới đây mang nhãn `?`: tên và mục đích là kiến thức chung; **tình trạng bảo trì, giấy phép và giá hiện hành chưa được kiểm tra**. Trước khi dựa vào một thư viện, hãy xem lần phát hành và hoạt động gần nhất trên trang GitHub/PyPI của nó.

### 8.1 Nền tảng

| Nền tảng | Dùng để |
|---|---|
| QuantConnect (động cơ mã nguồn mở LEAN) | Nghiên cứu, backtest và triển khai chiến lược trên nhiều loại tài sản |
| MetaTrader 5 + cộng đồng MQL5 (mql5.com) | Giao dịch FX/CFD bán lẻ; tài liệu, bài viết, kho mã, Strategy Tester |
| TradingView (Pine Script) | Vẽ biểu đồ và viết chỉ báo/chiến lược đơn giản |
| WorldQuant BRAIN, Numerai | Nền tảng nghiên cứu alpha / giải đấu dự báo (kiểm tra điều kiện tham gia) |
| Kaggle | Các cuộc thi dự báo thị trường do công ty giao dịch tổ chức (kiểm tra cuộc thi đang mở) |
| Interactive Brokers API, Alpaca, ccxt | Kết nối lập trình tới broker (cổ phiếu/phái sinh) và sàn tiền mã hóa |
| Quantopian | Từng là nền tảng cộng đồng nổi tiếng; **đã đóng cửa** (kiến thức chung — các bài giảng và Zipline vẫn được cộng đồng lưu giữ) |

### 8.2 Thư viện mã nguồn mở

| Nhóm | Thư viện | Mục đích |
|---|---|---|
| Backtest / giao dịch | LEAN; zipline-reloaded; backtrader; vectorbt; backtesting.py; NautilusTrader; hftbacktest | Backtest và chạy chiến lược (vector hóa hoặc event-driven; hftbacktest cho dữ liệu sổ lệnh) |
| Danh mục / rủi ro | Riskfolio-Lib; PyPortfolioOpt; skfolio | Tối ưu danh mục, đo rủi ro |
| Thống kê | statsmodels; arch | Chuỗi thời gian, hồi quy, GARCH |
| Phân tích hiệu suất | quantstats; pyfolio-reloaded; alphalens-reloaded | Báo cáo hiệu suất, phân tích nhân tố |
| Chỉ báo | TA-Lib; pandas-ta | Chỉ báo kỹ thuật |
| Định giá | QuantLib | Phái sinh, lãi suất |
| ML / RL | Qlib (Microsoft); FinRL | Nền tảng nghiên cứu ML và học tăng cường cho đầu tư |
| Crypto | ccxt; freqtrade | Kết nối sàn; bot giao dịch mã nguồn mở |

Lưu ý: *backtrader* được biết là ít cập nhật; *mlfinlab* từng mã nguồn mở nhưng được ghi nhận đã chuyển sang mô hình thương mại — cả hai điểm đều là kiến thức chung, cần kiểm tra lại.

## 9. Cộng đồng, blog và podcast

Tên là kiến thức chung (nhãn `?`); **mức độ còn hoạt động 2025–2026 chưa được kiểm tra**.

| Loại | Ví dụ |
|---|---|
| Hỏi đáp / diễn đàn | Quantitative Finance Stack Exchange; QuantNet; Wilmott forum; r/algotrading |
| Blog / nghiên cứu thực hành | Quantpedia; QuantStart; Quantocracy (tổng hợp blog); Alpha Architect; Robot Wealth; nghiên cứu công khai của AQR, Two Sigma, Man Institute |
| Podcast | Better System Trader; Chat With Traders; Top Traders Unplugged |

## 10. Nguồn dữ liệu để học

Mọi nguồn dữ liệu miễn phí đều có giới hạn về **giấy phép, chất lượng và survivorship bias** — đừng dùng chúng để kết luận về chiến lược rồi chạy tiền thật mà không kiểm tra chéo. Điều khoản và gói miễn phí **chưa được đối chiếu**.

| Nguồn | Ghi chú |
|---|---|
| Yahoo Finance (qua thư viện yfinance) | Tiện cho học tập; điều khoản sử dụng hạn chế dùng thương mại; dữ liệu có thể sai/thiếu |
| FRED (Cục Dự trữ Liên bang St. Louis) | Dữ liệu kinh tế vĩ mô, lãi suất |
| Stooq, Alpha Vantage, Tiingo, Polygon | Dữ liệu giá cổ phiếu/FX/crypto; gói miễn phí có giới hạn |
| data.binance.vision | Dữ liệu lịch sử công khai của Binance |
| Nasdaq Data Link (trước là Quandl) | Tập dữ liệu đa dạng, một phần trả phí |
| Dukascopy | Dữ liệu tick ngoại hối |
| Databento | Dữ liệu thị trường chất lượng cao, trả phí |
| Lịch sử giá của broker MT5 | Tiện nhất cho bot MT5 nhưng **khác nhau giữa các broker** và thường không đủ dài/sạch để kiểm định nghiêm túc |

## 11. Tại Việt Nam

**Cảnh báo về mức độ chưa kiểm chứng:** nhóm này **chưa được tra cứu xong** — hạn mức tìm kiếm cạn và truy cập trang của các trường, Ủy ban Chứng khoán bị chặn. Việc **chưa tìm thấy** thông tin không có nghĩa là Việt Nam *không có* chương trình hay cộng đồng tương ứng.

| Việc cần làm | Gợi ý |
|---|---|
| Tìm chương trình đào tạo định lượng trong nước | Tra trang tuyển sinh của các trường kinh tế, ngoại thương, bách khoa và các đại học quốc gia với các tên gọi **"Tài chính định lượng", "Toán tài chính", "Kỹ thuật tài chính", "Financial Engineering", "Quantitative Finance", "Data Science in Finance"** |
| Chứng chỉ chứng khoán trong nước | Trung tâm nghiên cứu và đào tạo chứng khoán của Ủy ban Chứng khoán Nhà nước; các hiệp hội nghề nghiệp (kiểm tra thông tin hiện hành) |
| Văn bằng online quốc tế (ví dụ WorldQuant University) | Kiểm tra việc công nhận văn bằng với cơ quan quản lý giáo dục trước khi đầu tư thời gian |
| Dữ liệu và API thị trường trong nước | Xem [05 — Thị trường Việt Nam](05-thi-truong-viet-nam.md), mục API của SSI, DNSE, TCBS |
| Cộng đồng và kênh tiếng Việt về quant/algo trading | **Chưa xác minh được** cộng đồng cụ thể nào; hãy tìm trực tiếp và áp dụng bảng "dấu hiệu cảnh báo" ở mục 13 |

## 12. Lộ trình học gợi ý (theo giai đoạn, không theo thời gian)

Tốc độ mỗi người khác nhau nên lộ trình dưới đây chia theo **sản phẩm đầu ra** thay vì số tháng. Chỉ sang giai đoạn kế tiếp khi đã có sản phẩm của giai đoạn trước.

| Giai đoạn | Mục tiêu | Học gì | Sản phẩm đầu ra (để biết đã xong) |
|---|---|---|---|
| **1. Nền tảng** | Hiểu dữ liệu và rủi ro | Xác suất – thống kê, đại số tuyến tính cơ bản, Python (pandas/numpy), lợi suất và rủi ro, phái sinh cơ bản | Notebook tính lợi suất, độ biến động, drawdown, Sharpe từ dữ liệu thật; giải thích được từng con số |
| **2. Backtest nghiêm ngặt** | Biết khi nào kết quả đáng tin | Tự viết backtester nhỏ; mô hình chi phí; in/out-of-sample; walk-forward; ghi số lần thử | Một chiến lược đơn giản có báo cáo gồm chi phí, out-of-sample và độ nhạy tham số |
| **3. Danh mục và rủi ro** | Từ một chiến lược đến một hệ thống | Định cỡ vị thế (volatility targeting, Kelly một phần), tương quan, giới hạn, drawdown | Danh mục vài chiến lược ít tương quan; giới hạn rủi ro viết thành văn bản |
| **4. Thực thi và vi cấu trúc** | Hiểu chi phí thật | Order book, spread, slippage, market impact, loại lệnh | Báo cáo slippage thật so với giả định; bộ lọc spread/thanh khoản |
| **5. Vận hành** | Chạy ổn định, quan sát được | Log/telemetry, cảnh báo, triển khai, bảo mật khóa API | Forward-test/paper đủ dài với log đầy đủ; kế hoạch xử lý sự cố |
| **6. Mở rộng** | Đào sâu theo hướng quan tâm | ML trong tài chính; phái sinh/volatility; dữ liệu thay thế; HFT/hạ tầng | Một dự án nghiên cứu có kiểm định chống overfitting |

Tiền thật chỉ nên vào **sau giai đoạn 5**, quy mô nhỏ, với giới hạn rủi ro đặt sẵn (xem checklist ở [03](03-yeu-to-cot-loi.md)).

## 13. Cách đánh giá một nguồn học hoặc sản phẩm quant

**Dấu hiệu cảnh báo** (thị trường giao dịch bán lẻ có nhiều nội dung bán khóa học/EA với lời hứa phóng đại):

1. Cam kết lợi nhuận cố định, "không thua lỗ", "lợi nhuận hàng tháng cao" mà không nói drawdown.
2. Chỉ có backtest đẹp; không có chi phí, out-of-sample hay forward-test được kiểm chứng độc lập.
3. Bán EA/bot "bí mật" mà không công bố logic và rủi ro; yêu cầu chuyển tiền, ủy quyền hoặc đưa mật khẩu tài khoản giao dịch.
4. Thúc ép mở tài khoản broker qua link giới thiệu (xung đột lợi ích).
5. Không dẫn nguồn học thuật: không có bài báo, sách, dữ liệu hay mã để tái lập.

**Dấu hiệu đáng tin hơn:** nêu rõ giả định và hạn chế; công bố mã/dữ liệu hoặc phương pháp để người khác tái lập; dẫn nguồn học thuật; thừa nhận giai đoạn thua lỗ; không hứa kết quả.

---
Trước: [01 — Quant trading là gì](01-quant-trading-la-gi.md) · Tiếp: [03 — Yếu tố cốt lõi](03-yeu-to-cot-loi.md) · [Mục lục](../README.md)
