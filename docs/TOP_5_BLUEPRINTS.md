# Flagship Engineering Execution Blueprints (Sections A to N)
## Top 5 Student-Led Deep-Tech Ventures for Jagdalpur B.Tech Engineering College

This document provides exhaustive, production-grade blueprints for the top 5 flagship ventures selected for immediate prototyping, institutional competition entry, and Bastar field pilot deployment.

---

# Flagship Contender #1: MahuaShilp
### *Clean Canopy Harvesting & Solar Rotary Micro-Dryers for Forest Livelihoods*

## Section A: Elevator Pitch (30 Seconds)
> Mahua collection causes over 60% of Bastar's dry-season forest fires because tribals burn fallen leaf litter to spot cream flowers on ash. This dirt contamination cuts selling prices by 45%. MahuaShilp deploys an elevated canopy catch-net that stops ground fires completely, paired with a portable solar-thermal rotary micro-dryer with NIR moisture feedback that cures flowers to export food-grade in 6 hours, doubling tribal farmgate income.

## Section B: Formal 2-Minute Competition/Investor Pitch
Respected Jury, every March across Central India, 350,000 tribal families enter dense Sal forests to harvest Mahua. To find the fallen flowers, they set fire to dry ground leaves—triggering thousands of devastating forest fires. The flowers that survive pick up dirt, dung, and sand. Sun-drying takes 5 days on dusty tracks, turning flowers black and sour. Tribals sell at distress rates of ₹30/kg for crude country liquor distillation.

We engineered MahuaShilp. First, an ultra-lightweight telescopic canopy net suspended under the Mahua tree catches flowers as they fall. Zero ground contact, zero leaf burning required. Second, our portable rotary micro-dryer uses a solar-assisted counter-flow warm air stream and an embedded Near-Infrared (NIR) optical moisture sensor. In just 6 hours, it cures the flowers to <12% moisture with zero caramelization and zero silica contamination.

Certified Grade-A food-grade Mahua sells to organic tea, energy bar, and craft beverage makers at ₹75/kg—more than doubling tribal income. At ₹24,500 per community unit, a Van Dhan Vikas Kendra recovers its cost in one single harvest season. We solve forest fires and poverty in one single engineering stroke.

## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)
- **Slide 1 - Hook & Local Urgency**: Video of Bastar forest fire triggered by leaf burning; ₹350 Cr regional Mahua economic loss.
- **Slide 2 - Problem Mechanics**: Why tribals burn leaves; dirt/silica contamination; 5-day fermentation during open sun-drying.
- **Slide 3 - The MahuaShilp Solution**: Canopy catch net (fire prevention) + Solar-assisted rotary drum micro-dryer (NIR feedback).
- **Slide 4 - Engineering Depth & Demo**: Live 60-second NIR moisture drop test on stage; perforated SS304 drum; adaptive PID curve.
- **Slide 5 - Unit Economics & Business Model**: B2G / B2B sales to 240 Bastar VDVKs @ ₹24,500/unit; 38% gross margin; mesh consumable recurring revenue.
- **Slide 6 - Market Size**: TAM ₹2,400 Cr national Mahua trade; SOM ₹28 Cr Bastar division over 3 years.
- **Slide 7 - Field Traction & Pilot**: Pilot partnership with Maa Danteshwari SHG Tokapal & TRIFOOD Park Jagdalpur.
- **Slide 8 - The Team & 90-Day Sprint**: Interdisciplinary B.Tech mechanical, electronics, and CS student innovators with local tribal roots.

## Section D: Complete Prototype Technical Architecture
- **Mechanical Subsystem**: Telescopic aluminum tension poles with 40-mesh monofilament net; perforated SS304 rotary drum (400mm dia x 600mm) driven by 12V 30W worm geared motor at 12 RPM.
- **Thermal Subsystem**: 150W PTC ceramic air heater element paired with a double-pass solar thermal air pre-heating collector box; 12V centrifugal blower (65 CFM).
- **Sensing And Control**: ESP32 DevKit V1 microcontroller; AMS AS7263 NIR 6-channel spectral sensor measuring 610-860nm absorption; Sensirion SHT31 ambient temp/RH sensor; 0.96-inch I2C OLED.
- **Power Subsystem**: 12V 100W monocrystalline solar panel charging a 12V 20Ah LiFePO4 battery pack via 10A MPPT charge controller.

## Section E: Itemized Bill of Materials (Total: ₹7,800)
| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |
|---|---|---|---|---|---|
| ESP32 DevKit V1 Board | Dual-core Xtensa 240MHz, Wi-Fi/BLE | 1 | ₹450 | Robu.in | ₹450 |
| AS7263 NIR Spectral Sensor | 6-channel NIR optical spectrometer I2C | 1 | ₹1,850 | Mouser / Robu | ₹1,850 |
| Perforated SS304 Drum | Custom fabricated 300x500mm 1.5mm perforated sheet | 1 | ₹1,600 | Local Jagdalpur Sheet Metal | ₹1,600 |
| 12V Worm Geared DC Motor | 12 RPM, 50 kg-cm high torque | 1 | ₹850 | Robu.in | ₹850 |
| PTC Air Heater 150W | 12V insulated PTC ceramic heater with fan | 1 | ₹550 | Amazon / Local Electricals | ₹550 |
| UV-Stabilized HDPE Mesh Net | 40-mesh 6m x 6m perimeter with eyelets | 1 | ₹950 | Agro-Net Supplier Raipur | ₹950 |
| Telescopic Support Poles | Lightweight aluminum 3-section 4m poles (set of 4) | 1 | ₹1,100 | Camping Gear Supplier | ₹1,100 |
| Sensirion SHT31 & OLED | Precision temp/humidity sensor + 0.96 OLED | 1 | ₹450 | Robu.in | ₹450 |

## Section F: 30-60-90 Day Execution Sprint Roadmap
### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):
- [ ] Finalize CAD design of rotary drum and fabricate sheet metal prototype in college workshop.
- [ ] Calibrate AS7263 NIR spectral sensor on varying moisture levels of re-hydrated Mahua flower samples.
- [ ] Implement PID thermal control loop on ESP32 to maintain strictly 42°C-45°C drying air.

### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):
- [ ] Integrate mechanical drum, heater, blower, and electronics into a ruggedized field-portable frame.
- [ ] Fabricate 3 full-scale canopy nets with quick-deploy tension clasps.
- [ ] Conduct 48-hour continuous endurance run in lab simulating full batch drying.

### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):
- [ ] Deploy 2 field units with Maa Danteshwari SHG in Tokapal block during seasonal harvest.
- [ ] Collect dried Mahua samples; test silica content and microbial purity at Bastar University food lab.
- [ ] Submit pilot results to Bastar DMF Trust and apply for DST NIDHI-PRAYAS prototype grant.

## Section G: First Customer Acquisition Playbook (Bastar Local)
- Direct pilot deployment with Maa Danteshwari Mahila SHG, Tokapal (free demonstration kit).
- Present certified Grade-A food-grade Mahua to TRIFOOD Processing Park Jagdalpur management.
- Demonstrate fire-prevention net to Divisional Forest Officer (DFO) Bastar to secure CAMPA/DMF sponsorship.

## Section H: Commercial Business Model & Unit Economics Deep Dive
- **Hardware Sales**: Selling community processing kit (Micro-dryer + 5 Canopy Nets) @ ₹24,500 to VDVKs and FPOs (COGS ₹14,800, Margin 39.6%).
- **Consumable Packs**: Annual replacement canopy nets and UV mesh @ ₹1,800 per pack.
- **Value Addition Royalty**: Aggregating certified food-grade Mahua from partner SHGs and selling to craft beverage companies (e.g., DesmondJi) and export confectioners with a ₹12/kg markup.

## Section I: 3-Year Scale-Up Trajectory
- **Year 1**: Deploy 60 units in Bastar Division via DMF Trust and incubation grants.
- **Year 2**: Scale to 280 units across Bastar, Dantewada, and Kondagaon through TRIFED Van Dhan Vikas Kendras.
- **Year 3**: Pan-state expansion with 1,000 units across Chhattisgarh, Odisha, and MP tribal belts.

## Section J: Critical Technical & Operational Risks
**Technical Vulnerabilities & Physics Constraints**:
- High natural sugar content in Mahua can caramelize and stick to drum perforations if temperature exceeds 50°C.
- Extreme sun exposure and abrasive handling tearing net eyelets in field forests.

**Commercial & Adoption Risks**:
- Short 8-week seasonal window risks machine underutilization during off-season.
- Traditional middlemen (kochis) attempting to block SHGs from selling independently.

## Section K: Intellectual Property & Patentable Claims
- Patent Claim 1: An elevated canopy tension net with radial shock-absorbing trunk collars for groundless forest flower harvesting.
- Patent Claim 2: A method and apparatus for real-time non-destructive NIR moisture-guided drying of Madhuca longifolia blossoms.

## Section L: Grant & Institutional Incubation Pathway
- Incubation at 36Inc Raipur (State Incubator) or IIT Bhilai Innovation Park.
- Apply for DST NIDHI-PRAYAS (₹10 Lakhs) for tooling and field fabrication.
- Apply for Bastar DMF Innovation Grant (₹15 Lakhs) for 50-panchayat field rollout.

---

# Flagship Contender #2: HemoPoint
### *Capillary Microfluidic Field Sickle Cell Quantifier for Tribal Missions*

## Section A: Elevator Pitch (30 Seconds)
> Over 15% of Bastar's indigenous population carries the sickle cell gene. Current field screening relies on visual solubility tests that confuse harmless carriers with life-threatening patients, while lab HPLC takes 3 weeks from Raipur. HemoPoint is a handheld optoelectronic reader with disposable microcapillary cartridges that analyzes sickle polymerisation kinetics in 3 minutes for ₹25, enabling on-the-spot differentiation of Trait (HbAS) from Disease (HbSS) right in forest sub-centers.

## Section B: Formal 2-Minute Competition/Investor Pitch
Distinguished Judges, Sickle Cell Disease is Central India's silent genetic tragedy. When two carriers marry, their children suffer excruciating bone crises, stroke, and early childhood death. Prime Minister Modi launched the National Sickle Cell Elimination Mission targeting 70 million screenings.

Here is the ground reality in Bastar: ANMs and ASHA workers use the chemical Solubility Test. It produces subjective cloudiness in a test tube. It CANNOT tell whether a child is a healthy carrier (HbAS) or has full-blown lethal disease (HbSS). Sending blood to Raipur for HPLC takes 3 to 4 weeks, by which time tribal families have disappeared into the forest.

We invented HemoPoint. It consists of a handheld optical reader and a ₹25 disposable microcapillary cartridge pre-dosed with a dry deoxygenating buffer. A 10 µL finger-prick blood drop is drawn by capillary action. The reader shines dual 660nm and 940nm pulsed LEDs through the channel. Over 180 seconds, our algorithm measures the exact kinetic velocity of hemoglobin polymer fiber formation. HbSS polymerizes exponentially; HbAS polymerizes linearly; HbAA stays flat.

In 3 minutes, the screen displays a definitive genetic classification and prints an ABHA-linked health slip. Our reader costs ₹18,000—not ₹20 Lakhs like HPLC—bringing gold-standard triage to the deepest forest village.

## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)
- **Slide 1 - National Priority**: PM Sickle Cell Elimination Mission; 15-25% Bastar carrier prevalence; severe infant mortality.
- **Slide 2 - The Diagnostic Gap**: Solubility test cannot differentiate HbAS from HbSS; HPLC centralized, expensive, and takes 3 weeks.
- **Slide 3 - The HemoPoint Innovation**: Microfluidic capillary cartridge + dual-wavelength turbidimetric kinetic curve analysis.
- **Slide 4 - Hardware & Kinetic Demo**: Live 3-minute curve trace on stage; V_max slope difference; instant LCD classification.
- **Slide 5 - Business Model & Consumable Moat**: Gillette razor-and-blade model: ₹18,000 reader + ₹25 disposable cartridges (65% margin).
- **Slide 6 - Market Sizing**: TAM ₹1,750 Cr national mission; SAM ₹280 Cr tribal belt; SOM ₹24 Cr Bastar division over 3 years.
- **Slide 7 - Clinical Validation Pathway**: Clinical correlation protocol with Dept of Pathology, Govt Medical College Jagdalpur.
- **Slide 8 - Regulatory & Grant Roadmap**: CDSCO Class B pathway; BIRAC BIG grant (₹50 Lakhs); Bastar DMF pilot support.

## Section D: Complete Prototype Technical Architecture
- **Optical Subsystem**: Light-tight black anodized aluminum manifold with narrow-band 660nm (isobestic) and 940nm (deoxy-HbS) pulsed LEDs; Hamamatsu S1223 PIN photodiode.
- **Analog Frontend**: LTC6268 ultralow input bias current (3 fA) transimpedance amplifier; Texas Instruments ADS1115 16-bit low-noise delta-sigma ADC.
- **Thermal Regulation**: Aluminum micro-cuvette heater block driven by a miniature PTC ceramic element and NTC thermistor maintaining exactly 37.0°C (+/- 0.1°C).
- **Compute And Ui**: ESP32-S3 SoC (8MB PSRAM); 2.4-inch SPI color LCD; integrated 58mm thermal micro-printer; BLE link to Ayushman Bharat Android app.

## Section E: Itemized Bill of Materials (Total: ₹6,500)
| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |
|---|---|---|---|---|---|
| ESP32-S3 DevKit Board | Dual-core Xtensa LX7 240MHz, 8MB PSRAM | 1 | ₹650 | Robu.in | ₹650 |
| Hamamatsu S1223 Photodiode | High-speed precision silicon PIN photodiode | 1 | ₹950 | Mouser Electronics | ₹950 |
| Precision Dual LEDs (660/940nm) | Narrow-band 20nm FWHM optical emitters | 2 | ₹220 | DigiKey / Mouser | ₹440 |
| LTC6268 Op-Amp & ADS1115 ADC | Low-bias TIA + 16-bit delta-sigma ADC | 1 | ₹850 | Mouser Electronics | ₹850 |
| 37°C Thermal Cuvette Block | Custom CNC aluminum block with PTC element | 1 | ₹750 | Local Precision CNC | ₹750 |
| Embedded 58mm Thermal Printer | TTL serial micro-printer mechanism | 1 | ₹1,450 | Robu.in | ₹1,450 |
| Laser-Cut PMMA Microfluidic Strips | Capillary channel chips with reagent (batch of 20) | 1 | ₹600 | Laser Fabrication Lab | ₹600 |
| 2.4-inch Color SPI LCD & Battery | 320x240 LCD + 3.7V 2500mAh Li-Po with BMS | 1 | ₹810 | Robu.in | ₹810 |

## Section F: 30-60-90 Day Execution Sprint Roadmap
### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):
- [ ] Fabricate optical manifold and assemble low-noise transimpedance amplifier circuit on custom PCB.
- [ ] Calibrate 660nm and 940nm transmission baseline using synthetic scattering phantoms (Formazin/milk).
- [ ] Code real-time sigmoidal curve-fitting algorithm on ESP32-S3.

### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):
- [ ] Optimize sodium metabisulfite / buffer dry-coating formulation inside PMMA microcapillary test channels.
- [ ] Integrate 37°C PID heater block, battery management, thermal printer, and color display into handheld enclosure.
- [ ] Execute repeatability testing on 100 test runs verifying zero baseline thermal drift.

### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):
- [ ] Initiate clinical correlation study on 50 pre-characterized blood samples at Govt Medical College Jagdalpur.
- [ ] Benchmark sensitivity and specificity against laboratory HPLC reports.
- [ ] Submit formal proposal to Bastar DMF Trust and BIRAC Biotechnology Ignition Grant (BIG).

## Section G: First Customer Acquisition Playbook (Bastar Local)
- Clinical validation with Dept of Pathology, Govt Medical College Jagdalpur.
- Demonstrate reader to Chief Medical & Health Officer (CMHO) Bastar for Sub-Health Centre screening.
- Secure Bastar DMF Trust project grant for equipping 25 high-prevalence tribal panchayat sub-centers.

## Section H: Commercial Business Model & Unit Economics Deep Dive
- **Hardware Sales**: Diagnostic reader sale @ ₹18,000 to NHM Chhattisgarh and District Health Societies (COGS ₹7,200, Margin 60%).
- **Consumable Cartridges**: High-volume supply of disposable test cartridges @ ₹25/test (Manufacturing cost ₹8.50, Gross margin 66%).
- **Data Reporting Api**: Cloud integration subscription for state Ayushman Bharat Sickle Cell Registry @ ₹2,400/year/reader.

## Section I: 3-Year Scale-Up Trajectory
- **Year 1**: Deploy 25 readers + 40,000 cartridges in Bastar Division via DMF grant.
- **Year 2**: Scale to 120 readers across Bastar Division + 250,000 cartridges.
- **Year 3**: Pan-state and national expansion across Central Indian tribal belt with 500 readers + 1.2M cartridges.

## Section J: Critical Technical & Operational Risks
**Technical Vulnerabilities & Physics Constraints**:
- Severe patient anemia (low starting hematocrit) shifting baseline light transmission.
- Reagent shelf-life degradation in humid tropical forest environments.

**Commercial & Adoption Risks**:
- Rigorous CDSCO medical device regulatory certification timelines.
- Bureaucratic delay in state health department tender disbursements.

## Section K: Intellectual Property & Patentable Claims
- Patent Claim 1: A point-of-care microfluidic turbidimetric cartridge and optical manifold for kinetic differentiation of sickle hemoglobin variants.
- Patent Claim 2: A ratiometric dual-wavelength algorithm for normalizing hematocrit variance during deoxygenation-induced hemoglobin polymerisation.

## Section L: Grant & Institutional Incubation Pathway
- Incubation at KIIT-TBI (Bhubaneswar) or IKP Knowledge Park (Hyderabad) for BioNEST MedTech support.
- Apply for BIRAC BIG (₹50 Lakhs) for full clinical trials and ISO 13485 compliance.
- Apply for Bastar DMF Innovation Grant (₹25 Lakhs) for direct district hospital deployment.

---

# Flagship Contender #3: FerroClear
### *Zero-Electricity Catalytic Aeration-Pyrolusite Iron Filtration for Tribal Schools*

## Section A: Elevator Pitch (30 Seconds)
> Tribal residential schools across Bastar and Dantewada pump groundwater poisoned with over 8.0 mg/L of iron from iron ore geology, turning school meals black and causing severe gastrointestinal illness. Existing government plants fail because no one manually backwashes valves or replenishes chemicals. FerroClear is a zero-electricity, chemical-free gravity filtration unit combining high-rate Venturi aeration with a catalytic pyrolusite sand bed and an engineered hydraulic bell siphon that automatically self-backwashes without human intervention, delivering safe water for under ₹15,000.

## Section B: Formal 2-Minute Competition/Investor Pitch
Members of the Jury, Bastar and Dantewada possess some of the richest iron ore deposits in the world. But beneath the feet of tribal children lies a toxic curse: groundwater with 3.0 to 12.0 mg/L of dissolved iron—up to 40 times the safe limit.

Walk into an Ashram Shala in Tokapal: the handpump water is orange; school water pipes are encrusted shut; midday dal turns inky black; children suffer chronic stomach pain and diarrhea. The government has installed iron removal plants, but walk around any village: 85% of them are completely dead. Why? Because they rely on daily chemical dosing (bleach) and complex manual multi-port backwash valves. In a school with one teacher and no plumber, valves get forgotten, media cokes into a solid rock, and the plant is abandoned.

We engineered FerroClear to be 100% human-independent and zero-electricity. As overhead tank water flows in, our custom Venturi aspirator vigorously sucks in atmospheric air, creating millions of micro-bubbles that rapidly oxidize ferrous iron into ferric precipitates. The water then cascades through a catalytic bed of graded pyrolusite sand—naturally active manganese dioxide ore—which strips iron down to <0.2 mg/L without adding any chemicals.

Now the breakthrough: How does it clean itself? We engineered a fluidic hydraulic bell siphon. As iron sludge accumulates, water level above the sand rises by a few centimeters. The instant it crests the siphon lip, the bell siphon automatically primes, sucking a torrent of clean water upward through the sand bed to backwash the sludge out the drain in 90 seconds, then resets itself! Zero electricity. Zero manual valves. Zero chemicals. Clean, crystal water for 500 schoolchildren every single day.

## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)
- **Slide 1 - Problem & Ground Evidence**: Hematitic geology; 8 mg/L toxic groundwater in 2,200 Bastar schools; failed manual IRP graveyard.
- **Slide 2 - The Engineering Innovation**: Multiphase Venturi aeration + Catalytic Pyrolusite MnO2 bed + Autonomous Hydraulic Bell Siphon.
- **Slide 3 - Physical Demonstration**: Spiked 8.0 mg/L brown water live filtration; automatic siphon backwash trigger; live chemical colorimetric test.
- **Slide 4 - Technical Specifications & Durability**: 1,000 LPH gravity flow; zero electricity; BIS IS-10500 compliance (<0.2 mg/L Fe).
- **Slide 5 - Business Model & Procurement Channels**: B2G sales under Jal Jeevan Mission & Bastar DMF Trust @ ₹16,500/unit; 42% gross margin.
- **Slide 6 - Market Size**: TAM ₹2,100 Cr Eastern/Central India iron belt; SAM ₹380 Cr; SOM ₹22 Cr Bastar division over 3 years.
- **Slide 7 - Field Deployment & Impact**: Pilot at Tokapal Tribal Ashram Shala; 500 children provided clean drinking water.
- **Slide 8 - The Team & Next Milestones**: Civil, mechanical, and chemical engineering student innovators; CSIR-NEERI validation roadmap.

## Section D: Complete Prototype Technical Architecture
- **Aeration Subsystem**: 3D-printed precision Venturi eductor nozzle (15mm throat) generating high air-to-water entrainment ratio (0.4) at 0.5 bar gravity head.
- **Reaction And Filtration Vessel**: Clear acrylic / rotomolded HDPE cylindrical vessel (150mm dia x 1200mm height) with stainless steel wedge-wire underdrain screen.
- **Catalytic Media Bed**: Multi-media graded bed: 150mm quartz pea gravel, 350mm high-purity pyrolusite (MnO2 > 75%) catalytic sand (0.8-1.2mm), 200mm fine silica sand (0.4-0.6mm).
- **Autonomous Siphon Engine**: Engineered PVC bell-siphon assembly with siphon break snorkel tube and anti-vortex crown triggering at 850mm hydraulic head.

## Section E: Itemized Bill of Materials (Total: ₹5,800)
| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |
|---|---|---|---|---|---|
| Clear Acrylic Test Cylinder | 150mm OD x 5mm wall x 1200mm height | 1 | ₹1,850 | Acrylic Fabricators Raipur | ₹1,850 |
| Catalytic Pyrolusite Media | Graded MnO2 active catalytic filter sand (25 kg) | 1 | ₹1,100 | Industrial Water Filter Media Supplier | ₹1,100 |
| Custom Venturi Aerator | 3D-printed PETG high-flow eductor nozzle | 1 | ₹450 | College 3D Print Lab | ₹450 |
| Hydraulic Bell Siphon Assembly | Engineered PVC pipe with siphon break tube | 1 | ₹550 | Plumbing Hardware Supplier | ₹550 |
| Graded Silica Sand & Gravel | Washed quartz silica sand + pea gravel (20 kg) | 1 | ₹350 | Local Water Treatment Supplier | ₹350 |
| Stainless Steel Wedge-Wire Screen | SS304 0.25mm slot underdrain plate | 1 | ₹650 | M/s Mesh Supplies | ₹650 |
| Valves, Manometer & Recirc Pump | CPVC ball valves + clear manometer + 12V demo pump | 1 | ₹850 | Local Hardware Store | ₹850 |

## Section F: 30-60-90 Day Execution Sprint Roadmap
### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):
- [ ] Fabricate transparent acrylic column and machine precision Venturi eductor nozzle.
- [ ] Benchmark dissolved oxygen transfer efficiency and Fe2+ to Fe3+ oxidation rates in environmental lab.
- [ ] Tune bell siphon geometry to achieve reliable siphon priming and clean shutoff under gravity flows.

### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):
- [ ] Pack catalytic pyrolusite sand bed and run 1,000-liter synthetic test cycles spiked to 10 mg/L iron.
- [ ] Verify effluent iron concentration consistently below 0.2 mg/L using spectrophotometric phenanthroline assay.
- [ ] Build full-scale rotomolded HDPE prototype unit rated for 1,000 Litres/Hour.

### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):
- [ ] Install pilot unit at Govt Tribal Boys Ashram Shala in Tokapal block.
- [ ] Conduct 30-day continuous water testing in collaboration with PHED District Water Quality Testing Laboratory, Jagdalpur.
- [ ] Present pilot compliance dossier to Executive Engineer PHED and Bastar DMF Trust.

## Section G: First Customer Acquisition Playbook (Bastar Local)
- Pilot installation at Govt Tribal Boys Ashram Shala, Tokapal (serving 250 resident students).
- Present water test verification certificates to District Collector Bastar and District Mineral Foundation Trust.
- Register technology under Jal Jeevan Mission innovation catalog for school water supply contracts.

## Section H: Commercial Business Model & Unit Economics Deep Dive
- **Hardware Sales**: Selling school/community filtration plants @ ₹16,500 to PHED, DMF, and CSR programs (COGS ₹9,500, Gross Margin 42.4%).
- **Media Replacement**: Supply of pre-packaged catalytic pyrolusite replenishment packs every 2 years @ ₹1,800/pack.
- **Installation And Amc**: Annual comprehensive water testing and pipeline maintenance contracts @ ₹2,200/year/school.

## Section I: 3-Year Scale-Up Trajectory
- **Year 1**: Deploy 100 units across Bastar residential schools via DMF Trust and CSR grants.
- **Year 2**: Scale to 450 units across Bastar, Dantewada, and Kanker districts.
- **Year 3**: Pan-state expansion with 1,800 units across Chhattisgarh and Odisha mining belts.

## Section J: Critical Technical & Operational Risks
**Technical Vulnerabilities & Physics Constraints**:
- Biological biofilm slime coating pyrolusite grains during extended vacation shutdowns.
- Siphon failing to prime if water inflow trickles below minimum hydraulic head velocity.

**Commercial & Adoption Risks**:
- Delayed institutional payments in government public health engineering tenders.
- Local plumbing contractors mis-aligning gravity head heights during field installation.

## Section K: Intellectual Property & Patentable Claims
- Patent Claim 1: A zero-electricity groundwater iron filtration apparatus with integral Venturi oxidation and autonomous hydraulic pulse-siphon backwash.
- Patent Claim 2: A self-regulating fluidic bell siphon configuration with anti-dribble atmospheric break for gravity-fed sand filtration beds.

## Section L: Grant & Institutional Incubation Pathway
- Incubation at 36Inc Raipur or IIT Bhilai Innovation Centre.
- Apply for Bastar DMF Innovation Grant (₹25 Lakhs) for school drinking water safety rollout.
- Apply for MSME Idea Hackathon 3.0 (₹15 Lakhs) for tooling rotomolded filter vessels.

---

# Flagship Contender #4: ConveyorGuard
### *Battery-Free Self-Powered Acoustic-Thermal Bearing Watcher for Ore Conveyors*

## Section A: Elevator Pitch (30 Seconds)
> At NMDC Nagarnar Steel and Bailadila iron ore mines, seized conveyor idler bearings generate friction temperatures exceeding 400°C, causing belt fires that cost over ₹5 Crores in plant shutdown. ConveyorGuard is a battery-free wireless sensor puck magnetically attached to idlers. Harvesting energy from roller vibration and heat, it combines contact vibration FFTs and non-contact infrared pyrometry to detect bearing cage micro-cracks weeks before seizure, alerting plant SCADA over an industrial mesh.

## Section B: Formal 2-Minute Competition/Investor Pitch
Good morning Jury, overland conveyor belts are the literal bloodline of India's steel and mining economy. At NMDC Bailadila and Nagarnar Steel Plant right here in Bastar, overland belts carry thousands of tons of abrasive iron ore across kilometers of rugged terrain. On a single 5-kilometer conveyor, there are over 10,000 rotating idler rollers.

When an idler roller bearing runs out of grease, it seizes. The heavy rubber belt keeps speeding at 4 meters per second over the stationary steel roller. The resulting friction ignites the belt. When a rubber belt catches fire, it burns for kilometers. A single conveyor fire costs between ₹2 to ₹5 Crores in damaged belting and causes catastrophic weeks of blast furnace shutdown. Manual patrol with handheld thermal guns in dust, rain, and heat is dangerous and catches bearings only when it's already too late.

We created ConveyorGuard. It is a rugged, IP68 cast-aluminum sensor puck that snaps onto the idler bracket using high-flux neodymium magnets. It has NO BATTERY to replace. It runs indefinitely by harvesting waste mechanical vibration using a piezoelectric cantilever and waste thermal gradient using a thermoelectric generator.

Inside the puck, an ultra-low-power DSP runs real-time vibration envelope FFTs to detect the subtle acoustic shockwaves of inner and outer raceway spalls (BPFO/BPFI frequencies), while a Melexis non-contact infrared sensor constantly watches roller surface temperature. If a bearing degrades, the puck broadcasts an alert through an industrial wireless mesh directly to the plant SCADA screen: 'Idler #C-04/R-842 Bearing Failure Imminent'. Plant engineers replace the roller during scheduled downtime. Zero fires. Zero downtime.

## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)
- **Slide 1 - Catastrophic Industrial Reality**: Conveyor belt friction fire videos; ₹5 Cr downtime at Nagarnar/Bailadila; DGMS safety circulars.
- **Slide 2 - Why Existing Monitoring Fails**: Manual thermal gun rounds miss sudden seizures; wired sensors get crushed by ore spillage; battery IoT dies in months.
- **Slide 3 - The ConveyorGuard Innovation**: Battery-free magnetic puck; hybrid piezo/TEG energy harvesting; dual acoustic FFT + non-contact IR thermopile.
- **Slide 4 - Benchtop Live Demonstration**: Motorized roller demo; apply friction brake; live IR temp spike + vibration FFT harmonic alert on SCADA in 5 seconds.
- **Slide 5 - Business Model & High ROI**: ₹4,800/puck + SCADA software license; sub-6-month payback (saving 1 fire pays for 5,000 sensors).
- **Slide 6 - Market Size**: TAM ₹2,800 Cr Indian heavy industry predictive maintenance; SAM ₹420 Cr; SOM ₹32 Cr Bastar steel/mining corridor.
- **Slide 7 - Enterprise Pilot Roadmap**: Trial deployment along Nagarnar Steel overland conveyor gallery with plant maintenance engineering.
- **Slide 8 - Team & Defensibility**: Mechatronics, DSP, and embedded firmware student innovators; industrial patent and ATEX certification pathway.

## Section D: Complete Prototype Technical Architecture
- **Energy Harvesting Power**: Mide Volture piezoelectric vibration cantilever harvester paired with a Linear Technology LTC3588-1 energy harvesting power management IC; 40mm TEG Peltier module harvesting thermal gradient into a 1.0F supercapacitor buffer.
- **Vibration And Acoustic Sensing**: Analog Devices ADXL345 high-bandwidth (3.2 kHz) digital accelerometer; contact acoustic resonant disc.
- **Thermal Sensing**: Melexis MLX90614 factory-calibrated infrared thermopile sensor (10-degree field of view).
- **Compute And Wireless Mesh**: Espressif ESP32-C3 RISC-V SoC running ESP-NOW self-healing wireless mesh protocol; AES-128 encrypted industrial packet broadcast.
- **Mechanical Chassis**: Milled aluminum block enclosure with IP68 O-ring silicone seal and dual N52 neodymium magnetic mounting feet.

## Section E: Itemized Bill of Materials (Total: ₹6,900)
| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |
|---|---|---|---|---|---|
| ESP32-C3 Mini Wireless Module | RISC-V 160MHz, 2.4GHz Wi-Fi/BLE/ESP-NOW | 1 | ₹320 | Robu.in | ₹320 |
| MLX90614 Infrared Temp Sensor | Non-contact factory-calibrated IR sensor | 1 | ₹950 | Robu.in | ₹950 |
| ADXL345 3-Axis Accelerometer | High-resolution digital vibration sensor | 1 | ₹220 | Robu.in | ₹220 |
| LTC3588 Energy Harvester Board | Piezoelectric power management module | 1 | ₹850 | Mouser Electronics | ₹850 |
| Piezo Cantilever & TEG Module | Vibration harvester beam + 40mm TEG | 1 | ₹1,150 | Robu.in / Techtonics | ₹1,150 |
| 5.5V 1.0F Supercapacitor | Low-ESR coin/radial supercapacitor buffer | 2 | ₹180 | Robu.in | ₹360 |
| N52 Neodymium Disc Magnets | 30mm dia x 5mm nickel-plated high-flux (pair) | 1 | ₹450 | Rare Earth Magnets India | ₹450 |
| Milled Aluminum Housing & Rig | IP68 enclosure + model test roller rig with motor | 1 | ₹2,600 | Local Jagdalpur Lathe Workshop | ₹2,600 |

## Section F: 30-60-90 Day Execution Sprint Roadmap
### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):
- [ ] Assemble energy harvesting circuit (LTC3588 + supercapacitor) and characterize power budget across varying vibration levels.
- [ ] Program bearing defect frequency (BPFO, BPFI, BSF) envelope extraction algorithms on ESP32-C3.
- [ ] Verify non-contact IR thermal accuracy against calibrated blackbody surface.

### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):
- [ ] Machine aluminum enclosure with magnetic mounting base and integrate all electronics.
- [ ] Construct benchtop conveyor roller test rig with motor drive and controllable friction brake.
- [ ] Implement self-healing multi-hop wireless mesh protocol with sub-second failover routing.

### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):
- [ ] Deploy 20 prototype sensor pucks along a test section of overland ore conveyor at NMDC Nagarnar Steel Plant.
- [ ] Interface wireless mesh gateway with plant SCADA dashboard over Modbus TCP.
- [ ] Apply for NMDC CSR Innovation Support and prepare patent provisional filing.

## Section G: First Customer Acquisition Playbook (Bastar Local)
- Field pilot with Conveyor Maintenance Division at NMDC Steel Limited (NSL), Nagarnar.
- Demonstrate technology to General Manager (Mechanical) NMDC Bailadila Iron Ore Complex, Kirandul.
- Present case study to Sponge Iron Manufacturers Association of Chhattisgarh.

## Section H: Commercial Business Model & Unit Economics Deep Dive
- **Hardware Sales**: Selling sensor pucks @ ₹4,800 to steel plants and mining operations (COGS ₹2,400, Gross Margin 50.0%).
- **Gateway And Network**: Mesh gateway units @ ₹35,000 per 2-kilometer conveyor segment.
- **Enterprise Predictive Saas**: Annual cloud/on-premise predictive maintenance software license @ ₹2,50,000/plant.

## Section I: 3-Year Scale-Up Trajectory
- **Year 1**: Deploy 400 pucks + 3 gateways at Nagarnar Steel and Bailadila mines.
- **Year 2**: Scale to 2,000 pucks across Central Indian mining, sponge iron, and cement plants.
- **Year 3**: Pan-India deployment of 7,500 pucks across Tata Steel, Coal India, and Adani Ports.

## Section J: Critical Technical & Operational Risks
**Technical Vulnerabilities & Physics Constraints**:
- Heavy abrasive iron dust and magnetic ore fines clinging to magnetic mounting puck.
- Extreme electromagnetic interference (EMI) from massive 500kW variable frequency drives (VFDs).

**Commercial & Adoption Risks**:
- Lengthy vendor onboarding and procurement cycles in public sector enterprises (NMDC).
- Competition from entrenched multinational instrumentation conglomerates (SKF, Emerson).

## Section K: Intellectual Property & Patentable Claims
- Patent Claim 1: A self-powered magnetic sensor node combining vibration-piezoelectric and thermal-gradient energy harvesting for industrial conveyor idlers.
- Patent Claim 2: A dual-parameter method for detecting conveyor idler seizure combining envelope FFT bearing fault harmonics with non-contact infrared thermal delta.

## Section L: Grant & Institutional Incubation Pathway
- Incubation at IIT Bhilai TIH (Technology Innovation Hub) or 36Inc Raipur.
- Apply for NMDC CSR Sustainable Development Innovation Grant (up to ₹30 Lakhs).
- Apply for DST NIDHI-PRAYAS (₹10 Lakhs) for tooling explosion-proof enclosures.

---

# Flagship Contender #5: BolBoli
### *Offline Multilingual Tribal Voice Terminal for Public Entitlements*

## Section A: Elevator Pitch (30 Seconds)
> Over 50% of elder forest tribals in Bastar speak only Gondi or Halbi and cannot read Devanagari text, leaving them vulnerable to corruption at PDS ration shops and Gram Panchayats where benefits are routinely skimmed. BolBoli is a solar-powered, offline, ruggedized voice-first terminal. Non-literate tribals tap their ration card, press a big red button, and ask in Halbi or Gondi: 'How much rice is left on my card?' The terminal answers audibly in their native tongue and prints an official anti-fraud receipt in 1 second without internet.

## Section B: Formal 2-Minute Competition/Investor Pitch
Respected Jury, India has built the world's most impressive digital welfare infrastructure—Aadhaar, PDS, MGNREGA, Direct Benefit Transfer. Yet, if you travel 40 kilometers from Jagdalpur into the forests of Lohandiguda, digital governance hits a brick wall.

More than half of tribal elders speak Halbi, Gondi, or Bhatra. They are completely illiterate in written Hindi or English script. When they walk into a Fair Price ration shop, the dealer tells them: 'The server is down; you only get 20 kilos this month instead of 35.' They have no smartphone, no 4G cellular signal in the forest valley, and no way to verify their legal quota. Millions of rupees of food grains and MGNREGA wages are systematically siphoned away from the poorest families in India.

We built BolBoli to give illiterate tribal citizens their own voice. BolBoli is a rugged, solar-powered wall-mounted terminal. There are no confusing touchscreens, no English menus, and NO DEPENDENCE ON THE INTERNET. A tribal mother taps her smart ration card on the NFC sensor and presses a large, illuminated tactile red button. She speaks in her native Halbi dialect: 'Moke ketla chaawal milbo?'

Inside the kiosk, an energy-efficient edge processor runs our custom quantized speech recognition and voice synthesizer model tuned on authentic Bastar tribal voice recordings. Within 800 milliseconds, completely offline, the kiosk's outdoor speaker speaks back warmly in fluent Halbi: 'Tumuk 35 kilo chawal milbo', and its built-in printer spits out an official slip with a tamper-evident QR code. She hands the slip to the ration dealer. Zero argument. Zero bribe. 100% of her food secured through local edge AI.

## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)
- **Slide 1 - The Digital Inclusion Paradox**: High-tech welfare portals vs illiterate Gondi/Halbi speakers; rampant welfare siphoning.
- **Slide 2 - Ground Reality in Bastar**: Zero 4G in valley forests; PDS ration leakage; tribal exploitation at rural ration shops.
- **Slide 3 - The BolBoli Innovation**: 100% offline edge speech AI in Gondi/Halbi; tactile big-button interface; audio response + printed slip.
- **Slide 4 - Live Offline Demonstration**: Physical terminal on stage; tap card; speak Halbi query; hear instant voice answer & printout.
- **Slide 5 - Technical Depth & Edge AI**: INT8 quantized acoustic models running on RK3588 NPU; noise-cancelling dual microphone array.
- **Slide 6 - Market Size & Public Procurement**: TAM ₹1,900 Cr national civic-tech; SAM ₹280 Cr tribal states; SOM ₹22 Cr Bastar division over 3 years.
- **Slide 7 - Institutional Pilot**: Deployment at Lohandiguda Gram Panchayat Fair Price Shop under District Food Controller supervision.
- **Slide 8 - Team & Social Impact**: Interdisciplinary B.Tech computer science, AI, and electronics team partnered with tribal linguistics scholars.

## Section D: Complete Prototype Technical Architecture
- **Compute Engine**: Orange Pi 5 Plus single-board computer powered by Rockchip RK3588 (8-core CPU with 6 TOPS hardware NPU, 8GB LPDDR4x RAM).
- **Acoustic Input**: Dual-microphone array board with hardware DSP acoustic echo cancellation and far-field beamforming (XMOS / Conexant chipset).
- **Audio Output**: Class-D high-efficiency audio amplifier (15W) driving an IP66 weatherproof outdoor horn loudspeaker.
- **Peripherals**: Industrial 60mm illuminated dome tactile pushbutton; Mifare RC522 RFID/NFC smart card reader; 58mm embedded high-speed thermal slip printer; 7-inch sunlight-readable IPS console.
- **Power And Casing**: 12V 10W monocrystalline solar panel with 12V 10Ah LiFePO4 battery pack and smart solar charger; 2mm mild-steel vandal-resistant powder-coated enclosure.

## Section E: Itemized Bill of Materials (Total: ₹8,500)
| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |
|---|---|---|---|---|---|
| Orange Pi 5 Plus (RK3588 8GB) | 8-Core CPU + 6 TOPS NPU SBC | 1 | ₹3,800 | Robu.in / OrangePi Official | ₹3,800 |
| Dual-Mic Noise-Cancelling Array | Far-field voice capture with DSP processor | 1 | ₹850 | Robu.in / Seeed Studio | ₹850 |
| Weatherproof 15W Outdoor Horn Speaker | High-efficiency wide-dispersion PA speaker | 1 | ₹750 | Local Audio Supplies Raipur | ₹750 |
| 58mm Embedded Thermal Slip Printer | TTL high-speed receipt printer with auto-cutter | 1 | ₹1,450 | Robu.in | ₹1,450 |
| Industrial 60mm Big Pushbutton | Illuminated tactile dome switch (Red) | 1 | ₹250 | Industrial Electricals | ₹250 |
| Mifare RC522 NFC Reader Module | 13.56 MHz RFID smart card reader | 1 | ₹180 | Robu.in | ₹180 |
| Vandal-Resistant Steel Enclosure | Custom fabricated 2mm sheet steel wall-mount box | 1 | ₹1,220 | Local Jagdalpur Steel Fabricators | ₹1,220 |

## Section F: 30-60-90 Day Execution Sprint Roadmap
### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):
- [ ] Collect and annotate 100 hours of spoken Halbi and Gondi conversational audio in collaboration with Bastar folk cultural societies.
- [ ] Quantize Whisper-tiny and Vosk speech models to INT8 precision and optimize for the RK3588 NPU using RKNN toolkit.
- [ ] Build acoustic test bench verifying speech recognition accuracy in 75dB simulated village market noise.

### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):
- [ ] Fabricate vandal-proof mild-steel kiosk chassis and integrate loudspeaker, big button, NFC reader, and thermal printer.
- [ ] Program offline sqlite entitlement caching database and local phonetic voice synthesis in Halbi.
- [ ] Conduct 100-user usability trials with non-literate tribal elders in Jagdalpur rural areas.

### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):
- [ ] Install pilot kiosk at Fair Price Shop in Lohandiguda block under supervision of District Food Officer.
- [ ] Measure grievance reduction and beneficiary satisfaction metrics over 30 days of ration distribution.
- [ ] Present project report to Department of Food & Civil Supplies Chhattisgarh and Bastar DMF Trust.

## Section G: First Customer Acquisition Playbook (Bastar Local)
- Pilot installation at Lohandiguda Gram Panchayat Fair Price Shop (serving 450 ration cardholders).
- Present demonstration to Secretary, Food & Civil Supplies Department Chhattisgarh.
- Secure Bastar DMF Trust civic-empowerment grant to equip 30 vulnerable forest panchayats.

## Section H: Commercial Business Model & Unit Economics Deep Dive
- **Hardware Sales**: Selling turnkey solar voice terminals @ ₹22,500 to Food & Civil Supplies and Panchayat departments (COGS ₹13,000, Margin 42.2%).
- **Software Updates And Amc**: Annual contract for localized dialect database updates, new welfare scheme rule additions, and printer paper supplies @ ₹2,200/year/kiosk.
- **Civic Analytics Dashboard**: Aggregated offline grievance analytics platform provided to District Collectorate @ ₹1,50,000/year.

## Section I: 3-Year Scale-Up Trajectory
- **Year 1**: Deploy 30 terminals in Bastar Division via DMF Trust and incubation grants.
- **Year 2**: Scale to 250 terminals across Bastar Division Fair Price Shops and Gram Panchayats.
- **Year 3**: Pan-state expansion with 1,200 terminals across Chhattisgarh, Odisha, and Jharkhand tribal corridors.

## Section J: Critical Technical & Operational Risks
**Technical Vulnerabilities & Physics Constraints**:
- High acoustic noise in crowded rural haat-bazaars masking speech input.
- Dialect drift and loan-word variance across different tribal hamlets.

**Commercial & Adoption Risks**:
- Political pushback or vandalism from corrupt ration dealers whose illicit profits are threatened.
- Delays in updating offline cached welfare databases in remote roadless locations.

## Section K: Intellectual Property & Patentable Claims
- Patent Claim 1: An offline, solar-powered speech-to-speech entitlement verification kiosk running quantized edge neural networks for non-literate indigenous dialects.
- Patent Claim 2: A method for verifying public distribution quotas via edge speech parsing and anti-tamper physical printed receipt generation without internet connectivity.

## Section L: Grant & Institutional Incubation Pathway
- Incubation at 36Inc Raipur or IIIT Naya Raipur TIDE Centre.
- Apply for MeitY TIDE 2.0 (₹7 Lakhs) for edge AI and speech hardware innovation.
- Apply for Bastar DMF Innovation Grant (₹20 Lakhs) for district-wide tribal welfare transparency.

---
