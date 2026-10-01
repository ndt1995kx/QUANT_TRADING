# 02 — Các kênh học thuật về quant trading

> Cập nhật: 2026-10-01 · Tài liệu giáo dục, **không phải tư vấn đầu tư** và không phải quảng cáo cho bất kỳ khóa học hay sản phẩm nào.

## 0. Cách đọc tài liệu này

**Nhãn đối chiếu** (cột "Đối chiếu"):

| Nhãn | Nghĩa |
|---|---|
| ✔ | Đã đối chiếu (tra cứu 10/2026): nội dung khớp với kết quả tìm kiếm trỏ tới trang chính thức |
| ? | Chưa đối chiếu được — dựa trên kiến thức chung hoặc dữ kiện không đủ chắc chắn |
| ✔ (gián tiếp) | Chỉ thấy qua nguồn thứ cấp (bài viết, tài liệu của bên thứ ba), chưa có nguồn chính thức |
| ✖ | Có dấu hiệu đã ngừng hoạt động |

**Giới hạn của lần tra cứu này — hãy đọc trước khi dựa vào số liệu:**

- Môi trường soạn thảo **không mở trực tiếp được trang gốc** (truy cập web bị chặn theo chính sách mạng) và hạn mức tìm kiếm bị cạn giữa chừng. Mọi nhãn ✔ nghĩa là *đã khớp với nội dung trang chính thức hiển thị trong kết quả tìm kiếm*, không phải *đã mở và đọc trang*. **Ngoại lệ:** ngày phát hành và commit của thư viện mã nguồn mở (mục 8.2, 11.2) được đọc trực tiếp từ GitHub/PyPI.
- **Giá, lịch thi, hạn nộp hồ sơ, ngày hội nghị** thay đổi thường xuyên. Chúng được ghi để tham khảo; luôn kiểm tra lại trên liên kết chính thức.
- Đào tạo chính quy và chứng chỉ **trong nước** ở Việt Nam (mục 11.1) **chưa được kiểm chứng**. Nhãn `?` đánh dấu những mục không tra được; hãy ưu tiên mở liên kết nguồn cho mục nào quan trọng với quyết định của bạn.

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

Tên sách, tác giả, nhà xuất bản và năm được đối chiếu **gián tiếp** qua nhiều trích dẫn BibTeX/README độc lập trên GitHub (chưa mở trang nhà xuất bản). Hãy kiểm tra lần xuất bản mới nhất trước khi mua.

| Tác giả | Tên | Nhà xuất bản, năm | Mức | Đáng đọc vì | Đối chiếu |
|---|---|---|---|---|---|
| Ernest P. Chan | *Quantitative Trading: How to Build Your Own Algorithmic Trading Business* | Wiley, 2008; bản 2: 2021 | Nhập môn | Dựng quy trình quant cá nhân gọn | ✔ |
| Rishi K. Narang | *Inside the Black Box* (bản 2, 2013: *A Simple Guide to Quantitative and High Frequency Trading*; bản 3, 2024: *A Simple Guide to Systematic Investing*) | Wiley | Nhập môn | Bản đồ các khối của một hệ quant | ✔ |
| Ernest P. Chan | *Algorithmic Trading: Winning Strategies and Their Rationale* | Wiley, 2013 | Trung cấp | Mean reversion / momentum kèm lý do kinh tế | ✔ |
| Ernest P. Chan | *Machine Trading: Deploying Computer Algorithms to Conquer the Markets* | Wiley, 2017 | Trung cấp | ML áp dụng thực chiến | ✔ |
| Lasse H. Pedersen | *Efficiently Inefficient* | Princeton UP, 2015 | Trung cấp | Chiến lược của quỹ và rủi ro thanh khoản | ✔ |
| Larry Harris | *Trading and Exchanges: Market Microstructure for Practitioners* | Oxford UP, 2003 | Trung cấp | Cách sàn, lệnh và thanh khoản vận hành | ✔ |
| Stefan Jansen | *Machine Learning for Algorithmic Trading* (bản 2) | Packt, 2020 | Trung cấp | Mã đầy đủ từ dữ liệu đến backtest. Kho mã của tác giả nay ghi bản 3 *Machine Learning for Trading* (2026); đã xuất bản hay chưa: chưa xác minh | ✔ (bản 2) |
| John C. Hull | *Options, Futures, and Other Derivatives* | Pearson | Trung cấp | Giáo trình phái sinh chuẩn | ? (bản mới nhất; bản 11 xác nhận gián tiếp) |
| Kakushadze & Serur | *151 Trading Strategies* | Palgrave Macmillan / Springer Nature, 2018 (SSRN 3247865) | Trung cấp | Danh mục công thức chiến lược. Toàn văn có miễn phí trên SSRN hay không: chưa xác minh | ✔ |
| Marcos López de Prado | *Advances in Financial Machine Learning* | Wiley, 2018 | Nâng cao | Purged CV, meta-labeling, chống overfitting | ✔ |
| Marcos López de Prado | *Machine Learning for Asset Managers* | Cambridge UP (Elements), 2020 | Nâng cao | Khử nhiễu ma trận hiệp phương sai, HRP/NCO | ✔ |
| Marcos López de Prado | *Causal Factor Investing* | Cambridge UP, 2023 (truy cập mở) | Nâng cao | Nhân quả thay vì tương quan trong đầu tư theo nhân tố | ✔ |
| Grinold & Kahn | *Active Portfolio Management* (bản 2) | McGraw-Hill, 2000 | Nâng cao | IC, breadth, "fundamental law" | ✔ |
| Roman Isichenko | *Quantitative Portfolio Management: The Art and Science of Statistical Arbitrage* | Wiley, 2021 | Nâng cao | Stat-arb hiện đại, chi phí giao dịch | ✔ |
| Cartea, Jaimungal & Penalva | *Algorithmic and High-Frequency Trading* | Cambridge UP, 2015 | Nâng cao | Thực thi tối ưu, market making | ✔ |
| Bouchaud, Bonart, Donier & Gould | *Trades, Quotes and Prices* | Cambridge UP, 2018 | Nâng cao | Vi cấu trúc thị trường thực nghiệm | ✔ |
| Steven Shreve | *Stochastic Calculus for Finance* (I, II) | Springer Finance, 2004 | Nâng cao | Nền toán định giá phái sinh | ✔ |
| Andrew W. Lo | *Adaptive Markets* | Princeton UP, 2017 | Đọc thêm | Khung "thị trường thích nghi" | ✔ |
| Emanuel Derman | *My Life as a Quant* | Wiley, 2004 | Đọc thêm | Nghề quant từ bên trong | ✔ |
| Gregory Zuckerman | *The Man Who Solved the Market* | 2019 | Đọc thêm | Renaissance Technologies (không phải sách kỹ thuật) | ✔ |

**Bài báo nên đọc** (về kiểm định chiến lược):

| Bài | Nơi đăng | Nội dung | Đối chiếu |
|---|---|---|---|
| Bailey & López de Prado, *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality* | Journal of Portfolio Management 40(5), 2014 (SSRN 2460551) | Hiệu chỉnh Sharpe khi đã thử nhiều chiến lược | ✔ |
| Bailey, Borwein, López de Prado & Zhu, *The Probability of Backtest Overfitting* | Journal of Computational Finance 20(4), 2017 (bản thảo SSRN 2326253) | Xác suất chiến lược tốt nhất trong mẫu lại kém ngoài mẫu | ✔ |
| Harvey, Liu & Zhu, *…and the Cross-Section of Expected Returns* | Review of Financial Studies 29(1), 2016 | Vì sao cần ngưỡng thống kê cao hơn khi đã thử hàng trăm nhân tố | ✔ |

## 8. Nền tảng thực hành, thư viện mã nguồn mở và cuộc thi

Danh sách mang tính **thông tin**, không phải khuyến nghị sử dụng. Ngày phát hành/commit của thư viện được **đọc trực tiếp từ GitHub/PyPI** (nguồn sơ cấp, tra cứu 10/2026); giá và điều khoản các nền tảng đối chiếu gián tiếp nên có thể đã đổi.

### 8.1 Nền tảng

| Nền tảng | Dùng để | Chi phí / điều kiện | Tình trạng | Đối chiếu |
|---|---|---|---|---|
| [QuantConnect](https://github.com/QuantConnect/Lean) (động cơ mã nguồn mở LEAN + dịch vụ đám mây) | Nghiên cứu, backtest, chạy live đa tài sản | Gói miễn phí: 1 node backtest (200 backtest/ngày) và 1 node research, **không** chạy live. Gói trả phí khởi điểm khoảng 84 USD/tháng, node live từ khoảng 24 USD/tháng (theo tài liệu chính thức 09/2026; một nguồn cũ ghi mức thấp hơn — hãy xem trang giá) | LEAN (Apache-2.0) hoạt động rất tích cực, commit 09/2026 | ✔ |
| QuantRocket | Nền tảng Python tự host (dựa trên Zipline/Moonshot) | Trả phí; giá chưa xác minh | Kho mã còn hoạt động 09/2026 | ✔ |
| WorldQuant BRAIN | Mô phỏng alpha; cuộc thi IQC; chương trình Consultant | Đăng ký miễn phí. IQC 2026: vòng loại 17/03–19/05, quỹ thưởng 100,000 USD. Consultant: được mời khi đạt ngưỡng điểm; danh sách quốc gia hỗ trợ có Việt Nam (nguồn gián tiếp) | Hoạt động 2026 | ✔ (gián tiếp) |
| Numerai | Dự báo dữ liệu ẩn danh, đặt cược bằng NMR | Tham gia miễn phí; stake bằng NMR. Kế hoạch 2026 chưa xác nhận | Hoạt động 2026 | ✔ (gián tiếp) |
| Alpaca | Broker API-first (cổ phiếu, ETF, quyền chọn, crypto), có paper trading | API giao dịch và paper miễn phí; dữ liệu cơ bản miễn phí (IEX, 200 yêu cầu/phút), gói dữ liệu trả phí khoảng 99 USD/tháng (nguồn thứ cấp). Mở tài khoản thật cho cư dân Việt Nam: **chưa xác minh** | `alpaca-py` 0.44.0 (08/2026, Apache-2.0); `alpaca-trade-api` đã cũ | ✔ (gián tiếp) |
| Interactive Brokers API | TWS API (Python, Java, C#, C++) | Phí API và điều kiện mở tài khoản từ Việt Nam: chưa xác minh | Kho chính thức cập nhật 09/2026; thư viện cộng đồng `ib_async` thay `ib_insync` | ✔ |
| MetaTrader 5 + gói Python | Nền tảng MT5, điều khiển bằng Python | Qua broker; phí chưa xác minh | Gói PyPI `MetaTrader5` 5.0.6231 (09/2026, MIT), cập nhật liên tục | ✔ |
| MQL5.community | Bài viết kỹ thuật, kho mã, Forge (Git) | Chưa kiểm | Bài viết còn đăng (05/2026); `forge.mql5.io` được dùng trong các kho mã 2026. Docs, Code Base, Signals, Market, Cloud Network: chưa tra được | ✔ (gián tiếp) |
| TradingView (Pine Script) | Chỉ báo và chiến lược trên TradingView | Chưa xác minh | Công cụ bên thứ ba 2026 nhắm Pine v5/v6 | ? |

**Cuộc thi Kaggle về dự báo thị trường — tất cả cuộc thi lớn tìm thấy đều đã kết thúc:** Jane Street (Market Prediction 2020–21; Real-Time Market Data Forecasting 10/2024–07/2025), Optiver (Realized Volatility 2021–22; Trading at the Close 2023–24), G-Research Crypto (kết thúc 05/2022), Hull Tactical (kết thúc 06/2026), MITSUI Commodity (kết thúc 01/2026). Không thấy cuộc thi quant nào đang mở trong chỉ mục khi tra cứu (✔, gián tiếp).

### 8.2 Thư viện mã nguồn mở

Dữ liệu ghi theo tháng/năm. Với thư viện **copyleft** (AGPL, GPL, LGPL), hãy đọc kỹ giấy phép nếu bạn định phân phối hoặc bán sản phẩm dựa trên chúng.

| Thư viện | Mục đích | Giấy phép | Phát hành / commit gần nhất | Bảo trì |
|---|---|---|---|---|
| QuantLib | Định giá phái sinh, lãi suất | BSD-3-Clause | 1.43 (07/2026); commit 09/2026 | Tích cực |
| zipline-reloaded | Backtest sự kiện (kế thừa Zipline của Quantopian) | Apache-2.0 | 3.1.1 (07/2025); commit 11/2025 | Thấp |
| backtrader | Backtest và chạy live | GPL-3.0+ | 1.9.78.123 (04/2023) | **Ngừng thực tế**; diễn đàn cộng đồng cũng đã chết |
| vectorbt | Backtest vector hóa | Apache-2.0 + Commons Clause | 1.1.1 (09/2026); 1.0 (04/2026) thêm engine Rust | Rất tích cực; có bản PRO trả phí riêng |
| backtesting.py | Backtest nhẹ | **AGPL-3.0** (copyleft mạnh) | 0.6.6 (07/2026) | Vừa |
| bt | Backtest phân bổ danh mục | MIT | 1.2.3 (09/2026) | Tích cực |
| NautilusTrader | Engine event-driven (Rust/Python) | LGPL-3.0+ | 1.231.0 ổn định (08/2026); 2.0.0rc5 (09/2026, tiền phát hành) | Rất tích cực |
| hftbacktest | Backtest HFT với dữ liệu sổ lệnh | MIT | 2.4.4 (12/2025) | Chậm (khoảng 9 tháng không commit) |
| Riskfolio-Lib | Tối ưu danh mục, đo rủi ro | BSD-3 | 7.3.0 (05/2026); commit 09/2026 | Tích cực |
| PyPortfolioOpt | Tối ưu danh mục | MIT | 1.6.0 (02/2026); commit 07/2026 | Vừa |
| skfolio | Danh mục theo kiểu scikit-learn | BSD-3 | 1.4.10 (09/2026) | Rất tích cực |
| statsmodels | Kinh tế lượng, chuỗi thời gian | BSD-3 | 0.15.0 (08/2026) | Tích cực |
| arch | GARCH, bootstrap | NCSA theo PyPI (tóm tắt GitHub ghi MIT — mâu thuẫn, hãy xem bản phát hành) | 8.0.0 (10/2025); commit 09/2026 | Tích cực |
| quantstats | Báo cáo hiệu suất | Apache-2.0 | 0.0.86 (09/2026) | Tích cực (vừa sửa lỗi tính toán 09/2026) |
| alphalens-reloaded, pyfolio-reloaded | Phân tích nhân tố, báo cáo danh mục | Apache-2.0 | 0.4.6 và 0.9.9 (06/2025) | Thấp |
| TA-Lib | Chỉ báo kỹ thuật | BSD-3-Clause | wrapper 0.8.1 (09/2026) | Tích cực |
| pandas-ta | Chỉ báo kỹ thuật | Không rõ | PyPI 0.4.71b0 (09/2025, beta); kho gốc `twopirllc/pandas-ta` trả 404 | **Bất định**; có fork `pandas-ta-classic` (MIT) |
| ccxt | Kết nối API nhiều sàn crypto | MIT | 4.5.84 (09/2026) | Rất tích cực |
| freqtrade | Bot giao dịch crypto | GPL-3.0 | 2026.9 (09/2026) | Rất tích cực |
| Qlib (Microsoft) | Nền tảng nghiên cứu ML cho đầu tư | MIT | 0.9.7 (08/2025); commit 09/2026 | Duy trì; dataset chính thức đang tạm tắt |
| FinRL | Học tăng cường cho tài chính | MIT | PyPI 0.3.7 (04/2024); commit 09/2026 | README: bản giáo dục/nghiên cứu; phát triển chuyển sang FinRL-X |
| mlfinlab | Công cụ theo López de Prado | "All rights reserved" | Không còn trên PyPI | **Thương mại**, không còn mã mở; có fork mở `mlfinpy` (MIT, alpha) |

Tất cả dòng trên: ✔ (đọc trực tiếp từ GitHub/PyPI), riêng *pandas-ta* mang nhãn `?` do trạng thái bất định.

### 8.3 Dự án từng nổi tiếng, nay ngừng hoặc đổi mô hình

Để người mới khỏi tốn thời gian:

- **Quantopian** (đóng cuối 2020) → kế thừa: zipline-reloaded, alphalens/pyfolio-reloaded (bảo trì thấp từ 06/2025), QuantRocket; bài giảng được cộng đồng lưu giữ. ✖
- **backtrader**: không có commit từ 04/2023; diễn đàn cộng đồng đã chết. ✖
- **ib_insync** (bản cuối 07/2023) → `ib_async`; **alpaca-trade-api** (bản cuối 01/2024) → `alpaca-py`.
- **mlfinlab**: từ mã mở sang đóng nguồn/thương mại.
- **pandas-ta**: kho gốc trả 404, PyPI chỉ còn bản beta 2025; có các fork.
- **Polygon.io** → **Massive** (đổi tên 30/10/2025); **Quandl** → **Nasdaq Data Link**.
- **Stooq**: dữ liệu CSV cần API key từ 03/2026 (theo một issue của pandas-datareader).
- **Qlib**: dataset chính thức tạm tắt; **FinRL**: phát triển chuyển sang FinRL-X.
- **Journal of Trading** và **Market Microstructure and Liquidity**: xem mục 2.2.

## 9. Cộng đồng, blog và podcast

Cột "Đối chiếu" dựa trên **dấu hiệu hoạt động 2025–2026 tìm thấy gián tiếp** (bài/tập mới), không phải đánh giá chất lượng.

| Nguồn | Dấu hiệu hoạt động | Đối chiếu |
|---|---|---|
| Quantpedia | Thư viện chiến lược; gói trả phí (Prime/Premium/Pro, hơn 900 chiến lược, có API) và khoảng 70 chiến lược miễn phí | ✔ (gián tiếp) |
| Quantocracy | Tổng hợp blog quant, còn đăng năm 2026 | ✔ (gián tiếp) |
| AQR (Data Library, Alternative Thinking) | Data Library cập nhật đến 05–06/2026 | ✔ (gián tiếp) |
| Two Sigma Insights; Man Institute | Còn xuất bản 2025–2026 | ✔ (gián tiếp) |
| Quantitative Finance Stack Exchange | Còn câu hỏi mới (09/2026) | ✔ (gián tiếp) |
| r/algotrading | Còn bài đăng (04/2026) | ✔ (gián tiếp) |
| Podcast: Better System Trader; Chat With Traders; Top Traders Unplugged | Còn phát hành (tập mới 09/2026) | ✔ (gián tiếp) |
| Discord của Freqtrade; diễn đàn QuantConnect; diễn đàn Alpaca | Còn hoạt động (08/2026) | ✔ (gián tiếp) |
| QuantStart, Robot Wealth, Alpha Architect, QuantNet, Wilmott, Elite Trader | Không có bằng chứng đủ tin về hoạt động 2025–2026 (QuantStart có dấu hiệu ít hoạt động) | ? |
| Diễn đàn cộng đồng backtrader | Không truy cập được | ✖ |

## 10. Nguồn dữ liệu để học

Mọi nguồn dữ liệu miễn phí đều có giới hạn về **giấy phép, chất lượng và survivorship bias** — đừng dùng chúng để kết luận về chiến lược rồi chạy tiền thật mà không kiểm tra chéo. Điều khoản và gói miễn phí đối chiếu gián tiếp nên có thể đã đổi.

| Nguồn | Điều khoản / gói (tra cứu 10/2026) | Cảnh báo | Đối chiếu |
|---|---|---|---|
| Yahoo Finance (thư viện `yfinance`) | Thư viện Apache-2.0 (1.7.0, 08/2026). README: không liên kết với Yahoo, dùng cho nghiên cứu/giáo dục; "API của Yahoo! Finance chỉ dành cho cá nhân" | Lấy dữ liệu không chính thức; bị giới hạn tốc độ; ngày công bố lợi nhuận kém tin cậy (nhiều lỗi được báo cáo 2025–26) | ✔ |
| FRED | Khóa API miễn phí; bắt buộc ghi thông báo "uses the FRED® API but is not endorsed…"; một số chuỗi của bên thứ ba có bản quyền | Kiểm tra bản quyền từng chuỗi | ✔ (gián tiếp) |
| Stooq | CSV miễn phí nhưng từ 03/2026 cần API key; không có điều khoản/SLA | Chỉ nên dùng làm dự phòng | ✔ (gián tiếp) |
| Alpha Vantage | Khóa miễn phí: 25 yêu cầu/ngày, 5 yêu cầu/phút; điều khoản tách cá nhân phi thương mại và thương mại | Không đủ để quét nhiều mã | ✔ (gián tiếp) |
| Tiingo | Gói miễn phí giới hạn (khoảng 1,000 yêu cầu/ngày, 500 mã/tháng — tài liệu thứ cấp) | Giá và giới hạn chưa đối chiếu trang gốc | ✔ (gián tiếp) |
| Polygon.io (nay là Massive) | Đổi tên Massive.com ngày 30/10/2025; khóa cũ vẫn dùng; gói miễn phí giới hạn | Tên miền API đổi từ `api.polygon.io` sang `api.massive.com` | ✔ |
| data.binance.vision | Dữ liệu spot/futures công khai (klines, trades) kèm checksum; kho mã MIT + điều khoản sử dụng | Chỉ một sàn; đọc điều khoản | ✔ |
| Nasdaq Data Link (trước là Quandl) | Cần khóa API; bộ dữ liệu miễn phí/trả phí hiện hành chưa xác minh | Client Python cũ (08/2022) | ? |
| Dukascopy | Tick FX/CFD miễn phí qua công cụ bên thứ ba; điều khoản gốc chưa mở được | Kiểm tra điều khoản trước khi dùng thương mại | ? |
| Databento | Trả phí theo mức sử dụng; có credit dùng thử cho tài khoản mới (nguồn thứ cấp) | Giá chưa đối chiếu trang gốc | ✔ (gián tiếp) |
| Lịch sử giá của broker MT5 | Tiện nhất cho bot MT5 | **Khác nhau giữa các broker**; chưa kiểm chất lượng | ? |

**Cảnh báo chung:** Yahoo, Alpaca và Stooq chủ yếu phục vụ danh sách mã **đang niêm yết** — mã đã hủy niêm yết biến mất (**survivorship bias**; ước lượng thứ cấp cho thấy tác động có thể đáng kể). Feed IEX miễn phí của Alpaca chỉ chiếm một phần nhỏ khối lượng hợp nhất (ước lượng thứ cấp khoảng vài %). Dữ liệu MT5 phụ thuộc broker.

## 11. Tại Việt Nam

### 11.1 Đào tạo chính quy và chứng chỉ trong nước — chưa kiểm chứng

Phần này **chưa được tra cứu xong**: hạn mức tìm kiếm cạn và truy cập trang của các trường, Ủy ban Chứng khoán bị chặn. Việc **chưa tìm thấy** không có nghĩa là Việt Nam *không có* chương trình tương ứng.

| Việc cần làm | Gợi ý |
|---|---|
| Tìm chương trình đào tạo định lượng trong nước | Tra trang tuyển sinh của các trường kinh tế, ngoại thương, bách khoa và đại học quốc gia với các tên gọi **"Tài chính định lượng", "Toán tài chính", "Kỹ thuật tài chính", "Financial Engineering", "Quantitative Finance", "Data Science in Finance"** |
| Chứng chỉ chứng khoán trong nước | Trung tâm nghiên cứu và đào tạo chứng khoán của Ủy ban Chứng khoán Nhà nước; các hiệp hội nghề nghiệp (kiểm tra thông tin hiện hành) |
| Văn bằng online quốc tế (ví dụ WorldQuant University) | Kiểm tra việc công nhận văn bằng với cơ quan quản lý giáo dục trước khi đầu tư thời gian |

### 11.2 Thư viện, dữ liệu và cộng đồng mã nguồn mở bằng tiếng Việt

Tìm thấy qua GitHub/PyPI (nguồn sơ cấp, tra cứu 10/2026). Danh sách mang tính thông tin, **không phải khuyến nghị**; hãy tự kiểm tra giấy phép, điều khoản và độ tin cậy trước khi dùng. API **giao dịch** của các công ty chứng khoán (SSI, DNSE, TCBS…) xem [05 — Thị trường Việt Nam](05-thi-truong-viet-nam.md), mục 4.

| Tên | Loại / giấy phép | Tình trạng | Đối chiếu |
|---|---|---|---|
| **vnstock** | Thư viện dữ liệu chứng khoán Việt Nam. Giấy phép riêng *license-2026.09* (mã nguồn mở nhưng **không phải** giấy phép OSI): miễn phí cho cá nhân/học tập/nghiên cứu; cần thỏa thuận riêng nếu phân phối lại hoặc làm sản phẩm bán quyền truy cập dữ liệu. Hạn mức theo cấp: khách 20 lượt gọi/phút; cộng đồng 60 (đăng ký miễn phí lấy API key); cấp tài trợ 180–600. Giấy phép cũ (vnstock3) cấm thương mại và có telemetry ẩn danh | Bản 4.0.9 (09/2026); nguồn dữ liệu VCI, KBS, MSN, FMarket (TCBS bị gỡ từ 03/2026). **Lưu ý:** gói `vnstock` trên PyPI đang ở trạng thái "quarantined" (lý do chưa rõ) và README hướng dẫn cài từ một index riêng — hãy cân nhắc rủi ro chuỗi cung ứng và kiểm tra nguồn gói trước khi cài | ✔ |
| **QuantVN** | Dự án quant mở + thư viện `quantvn` (cổ phiếu Việt Nam, phái sinh VN30, crypto Binance); MIT; cần API key của nền tảng | Bản 0.1.25 (07/2026, alpha); commit 09/2026 | ✔ |
| **XNO Quant** | Cộng đồng + thư viện `xnoapi` (cổ phiếu, VN30F1M/F2M, quỹ, forex/crypto); MIT; cần API key | Bản 0.1.28 (10/2025); cập nhật chậm; có chuỗi webinar. Mức hoạt động của nhóm cộng đồng chưa kiểm | ✔ |
| **vnquant** | Lấy giá và báo cáo tài chính từ các trang tin tài chính trong nước; MIT; cài từ GitHub | Bảo trì thấp (2025) | ✔ |
| **vietfin** | Thư viện/CLI dữ liệu Việt Nam | Commit cuối 04/2024 — ngừng thực tế | ✖ |
| **FiinQuant / FiinQuantX** (FiinGroup) | Thư viện Python dữ liệu thời gian thực, lịch sử, báo cáo tài chính (HOSE/HNX/UPCoM); **trả phí** (các gói Basic/Advanced/Professional; số tiền chưa xác minh); cần tài khoản | Kho chính thức cập nhật 09/2026 | ✔ (gián tiếp) |
| **SSI FastConnect Data** (iBoard) | API dữ liệu thời gian thực cơ sở/phái sinh; lấy consumerID/secret trên iBoard; theo trang SSI là miễn phí, kích hoạt tại phòng giao dịch (chưa mở trang gốc) | SDK `ssi-fc-data` 2.2.2 (06/2024) — cập nhật chậm | ✔ (gián tiếp) |
| Vietstock, CafeF (dịch vụ dữ liệu) | Chưa xác minh gói và giá | — | ? |
| Cộng đồng MT5/MQL5 tiếng Việt; kênh YouTube, blog, diễn đàn quant tiếng Việt | **Không tìm thấy** qua công cụ khả dụng (không tra được Facebook/YouTube) — không có nghĩa là không có | — | ? |

Một số dự án trên có nhóm cộng đồng trên Facebook ghi trong README của dự án; mức hoạt động **chưa kiểm** — hãy áp dụng bảng "dấu hiệu cảnh báo" ở mục 13 khi tham gia.

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
