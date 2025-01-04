
import json


_disclosure_requirement_points = {
   'E1-1_14' : """
      - **Point 14:** The undertaking shall disclose its transition plan for climate change mitigation.
   """,
   
   'E1-1_15' : """
      - **Point 15:** The objective of this Disclosure Requirement is to enable an understanding of the undertaking’s past, current, and future mitigation efforts to ensure that its strategy and business model are compatible with the transition to a sustainable economy, and with the limiting of global warming to 1.5 °C in line with the Paris Agreement and with the objective of achieving climate neutrality by 2050 and, where relevant, the undertaking’s exposure to coal, oil and gas-related activities.
   """,
   'E1-1_16' : """
      - **Point 16:** The information required by paragraph 14 shall include:
         -(a) by reference to GHG emission reduction targets (as required by Disclosure Requirement E1-4), an explanation of how the undertaking’s targets are compatible with the limiting of global warming to 1.5°C in line with the Paris Agreement;
         -(b) by reference to GHG emission reduction targets (as required by Disclosure Requirement E1-4) and the climate change mitigation actions (as required by Disclosure Requirement E1-3), an explanation of the decarbonisation levers identified, and key actions planned, including changes in the undertaking’s product and service portfolio and the adoption of new technologies in its own operations, or the upstream and/or downstream value chain;
         -(c) by reference to the climate change mitigation actions (as required by Disclosure Requirement E1-3), an explanation and quantification of the undertaking’s investments and funding supporting the implementation of its transition plan, with a reference to the key performance indicators of taxonomy-aligned CapEx, and where relevant the CapEx plans, that the undertaking discloses in accordance with Commission Delegated Regulation (EU) 2021/2178;
         -(d) a qualitative assessment of the potential locked-in GHG emissions from the undertaking’s key assets and products. This shall include an explanation of if and how these emissions may jeopardise the achievement of the undertaking’s GHG emission reduction targets and drive transition risk , and if applicable, an explanation of the undertaking’s plans to manage its GHG-intensive and energy-intensive assets and products;
         -(e) for undertakings with economic activities that are covered by delegated regulations on climate adaptation or mitigation under the Taxonomy Regulation, an explanation of any objective or plans (CapEX, CapEx plans, OpEX) that the undertaking has for aligning its economic activities (revenues, CapEx, OpEx) with the criteria established in Commission Delegated Regulation 2021/2139;
         -(f) if applicable, a disclosure of significant CapEx amounts invested during the reporting period related to coal, oil and gas-related economic activities;
         -(g) a disclosure on whether or not the undertaking is excluded from the EU Paris-aligned Benchmarks;
         -(h) an explanation of how the transition plan is embedded in and aligned with the undertaking’s overall business strategy and financial planning;
         -(i) whether the transition plan is approved by the administrative, management and supervisory bodies ; and
         -(j) an explanation of the undertaking’s progress in implementing the transition plan.
   """,
   'E1-1_17' : """
      - **Point 17:** In case the undertaking does not have a transition plan in place, it shall indicate whether and, if so, when it will adopt a transition plan.
   """,
   'E1-1_18' : """
   Material impacts, risks and opportunities and their interaction with strategy and business model
      - **Point 18:** The undertaking shall explain for each material climate-related risk it has identified, whether the entity considers the risk to be a climate-related physical risk or climate-related transition risk .
   """,
   'E1-1_19' : """
      - **Point 19:** The undertaking shall describe the resilience of its strategy and business model in relation to climate change. This description shall include:
         -(a) the scope of the resilience analysis;
         -(b) how and when the resilience analysis has been conducted, including the use of climate scenario analysis as referenced in the Disclosure Requirement related to ESRS 2 IRO-1 and the related application requirement paragraphs; and
         -(c) the results of the resilience analysis including the results from the use of scenario analysis.
   """,
   'E1-1_20' : """
   Impact, risk and opportunity management
      - **Point 20:** The undertaking shall describe the process to identify and assess climate-related impacts, risks and opportunities . This description shall include its process in relation to:
         -(a) impacts on climate change, in particular, the undertaking’s GHG emissions (as required by Disclosure Requirement ESRS E1-6);
         -(b) climate-related physical risks in own operations and along the upstream and downstream value chain , in particular:
           i.   the identification of climate-related hazards, considering at least high emission climate scenarios ; and
           ii.  the assessment of how its assets and business activities may be exposed and are sensitive to these climate-related hazards, creating gross physical risks for the undertaking.
         -(c) climate-related transition risks and opportunities in own operations and along the upstream and downstream value chain , in particular:
           i.   the identification of climate-related transition events, considering at least a climate scenario in line with limiting global warming to 1.5°C with no or limited overshoot; and
           ii.  the assessment of how its assets and business activities may be exposed to these climate-related transition events, creating gross transition risks or opportunities for the undertaking.
   """,
   'E1-1_21' : """
      - **Point 21:** When disclosing the information required under paragraphs 20 (b)and 20 (c) the undertaking shall explain how it has used climate-related scenario analysis, including a range of climate scenarios, to inform the identification and assessment of physical risks and transition risks and opportunities over the short-, medium- and long-term.
   """,
   'E1-2_22' : """
      - **Point 22:** The undertaking shall describe its policies adopted to manage its material impacts , risks and opportunities related to climate change mitigation and adaptation .
   """,
   'E1-2_23' : """
      - **Point 23:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of its material climate change mitigation and adaptation impacts, risks and opportunities.
   """,
   'E1-2_24' : """
      - **Point 24:** The disclosure required by paragraph 22 shall contain the information on the policies the undertaking has in place to manage its material impacts, risks and opportunities related to climate change mitigation and adaptation in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters .
   """,
   'E1-2_25' : """
      - **Point 25:** The undertaking shall indicate whether and how its policies address the following areas:
         -(a) climate change mitigation ;
         -(b) climate change adaptation ;
         -(c) energy efficiency;
         -(d) renewable energy deployment; and
         -(e) other
   """,
   'E1-3_26' : """
      - **Point 26:** The undertaking shall disclose its climate change mitigation and adaptation actions and the resources allocated for their implementation.
   """,
   'E1-3_27' : """
      - **Point 27:** The objective of this Disclosure Requirement is to provide an understanding of the key actions taken and planned to achieve climate-related policy objectives and targets.
   """,
   'E1-3_28' : """
      - **Point 28:** The description of the actions and resources related to climate change mitigation and adaptation shall follow the principles stated in ESRS 2 MDR-A Actions and resources in relation to material sustainability matters .
   """,
   'E1-3_29' : """
      - **Point 29:** In addition to ESRS 2 MDR-A, the undertaking shall:
         -(a) when listing key actions taken in the reporting year and planned for the future, present the climate change mitigation actions by decarbonisation lever including the nature- based solutions;
         -(b) when describing the outcome of the actions for climate change mitigation, include the achieved and expected GHG emission reductions ; and
         -(c) relate significant monetary amounts of CapEx and OpEx required to implement the actions taken or planned to:
           i.   the relevant line items or notes in the financial statements;
           ii.  the key performance indicators required under Commission Delegated Regulation (EU) 2021/2178; and
           iii. if applicable, the CapEx plan required by Commission Delegated Regulation (EU) 2021/2178.
   """,
   'E1-4_30' : """
      - **Point 30:** The undertaking shall disclose the climate-related targets it has set.
   """,
   'E1-4_31' : """
      - **Point 31:** The objective of this Disclosure Requirement is to enable an understanding of the targets the undertaking has set to support its climate change mitigation and adaptation policies and address its material climate-related impacts, risks and opportunities.
   """,
   'E1-4_32' : """
      - **Point 32:** The disclosure of the targets required in paragraph 30 shall contain the information required in ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets .
   """,
   'E1-4_33' : """
      - **Point 33:** For the disclosure required by paragraph 30, the undertaking shall disclose whether and how it has set GHG emissions reduction targets and/or any other targets to manage material climate-related impacts, risks and opportunities , for example, renewable energy deployment, energy efficiency, climate change adaptation , and physical or transition risk mitigation.
   """,
   'E1-4_30' : """
      - **Point 34:** If the undertaking has set GHG emission reduction targets ( 39 ) , ESRS 2 MDR-T and the following requirements shall apply:
         -(a) GHG emission reduction targets shall be disclosed in absolute value (either in tonnes of CO2eq or as a percentage of the emissions of a base year) and, where relevant, in intensity value;
         -(b) GHG emission reduction targets shall be disclosed for Scope 1, 2 , and 3 GHG emissions, either separately or combined. The undertaking shall specify, in case of combined GHG emission reduction targets , which GHG emission Scopes (1, 2 and/or 3) are covered by the target, the share related to each respective GHG emission Scope and which GHGs are covered. The undertaking shall explain how the consistency of these targets with its GHG inventory boundaries is ensured (as required by Disclosure Requirement E1-6). The GHG emission reduction targets shall be gross targets, meaning that the undertaking shall not include GHG removals, carbon credits or avoided emissions as a means of achieving the GHG emission reduction targets;
         -(c) the undertaking shall disclose its current base year and baseline value, and from 2030 onwards, update the base year for its GHG emission reduction targets after every five-year period thereafter. The undertaking may disclose the past progress made in meeting its targets before its current base year provided that this information is consistent with the requirements of this Standard;
         -(d) GHG emission reduction targets shall at least include target values for the year 2030 and, if available, for the year 2050. From 2030, target values shall be set after every 5-year period thereafter;
         -(e) the undertaking shall state whether the GHG emission reduction targets are science- based and compatible with limiting global warming to 1.5°C. The undertaking shall state which framework and methodology has been used to determine these targets including whether they are derived using a sectoral decarbonisation pathway and what the underlying climate and policy scenarios are and whether the targets have been externally assured. As part of the critical assumptions for setting GHG emission reduction targets, the undertaking shall briefly explain how it has considered future developments (e.g., changes in sales volumes, shifts in customer preferences and demand, regulatory factors, and new technologies) and how these will potentially impact both its GHG emissions and emissions reductions; and
         -(f) the undertaking shall describe the expected decarbonisation levers and their overall quantitative contributions to achieve the GHG emission reduction targets (e.g., energy or material efficiency and consumption reduction, fuel switching, use of renewable energy , phase out or substitution of product and process).
   """,
   'E1-5_35' : """
      - **Point 35:** The undertaking shall provide information on its energy consumption and mix.
   """,
   'E1-5_36' : """
      - **Point 36:** The objective of this Disclosure Requirement is to provide an understanding of the undertaking’s total energy consumption in absolute value, improvement in energy efficiency, exposure to coal, oil and gas-related activities, and the share of renewable energy in its overall energy mix.
   """,
   'E1-5_37' : """
      - **Point 37:** The disclosure required by paragraph 35 shall include the total energy consumption in MWh related to own operations disaggregated by:
         -(a) total energy consumption from fossil sources
         -(b) total energy consumption from nuclear sources;
         -(c) total energy consumption from renewable sources disaggregated by:
           i.   fuel consumption for renewable sources including biomass (also comprising industrial and municipal waste of biologic origin), biofuels, biogas, hydrogen from renewable sources ( 41 ) , etc.;
           ii.  consumption of purchased or acquired electricity, heat, steam, and cooling from renewable sources; and
           iii. consumption of self-generated non-fuel renewable energy.
   """,
   'E1-5_38' : """
      - **Point 38:** The undertaking with operations in high climate impact sectors ( 42 ) shall further disaggregate their total energy consumption from fossil sources by:
         -(a) fuel consumption from coal and coal products;
         -(b) fuel consumption from crude oil and petroleum products;
         -(c) fuel consumption from natural gas;
         -(d) fuel consumption from other fossil sources;
         -(e) consumption of purchased or acquired electricity, heat, steam, or cooling from fossil sources;
   """,
   'E1-5_39' : """
      - **Point 39:** In addition, where applicable, the undertaking shall disaggregate and disclose separately its non-renewable energy production and renewable energy production in MWh.
   """,
   'E1-5_40' : """
      Energy intensity based on net revenue
      - **Point 40:** The undertaking shall provide information on the energy intensity (total energy consumption per net revenue) associated with activities in high climate impact sectors .
   """,
   'E1-5_41' : """
      - **Point 41:** The disclosure on energy intensity required by paragraph 40 shall only be derived from the total energy consumption and net revenue from activities in high climate impact sectors .
   """,
   'E1-5_42' : """
      - **Point 42:** The undertaking shall specify the high climate impact sectors that are used to determine the energy intensity required by paragraph 40.
   """,
   'E1-5_43' : """
      - **Point 43:** The undertaking shall disclose the reconciliation to the relevant line item or notes in the financial statements of the net revenue amount from activities in high climate impact sectors (the denominator in the calculation of the energy intensity required by paragraph 40).
   """,
   'E1-6_44' : """
      - **Point 44:** The undertaking shall disclose in metric tonnes of CO2eq its
         -(a) gross Scope 1 GHG emissions;
         -(b) gross Scope 2 GHG emissions;
         -(c) gross Scope 3 GHG emissions; and
         -(d) total GHG emissions.
   """,
   'E1-6_45' : """
      - **Point 45:** The objective of the Disclosure Requirement in paragraph 44 in respect of:
         -(a) gross Scope 1 GHG emissions as required by paragraph 44 (a) is to provide an understanding of the direct impacts of the undertaking on climate change and the proportion of its total GHG emissions that are regulated under emission trading schemes.
         -(b) gross Scope 2 GHG emissions as required by paragraph 44 (b) is to provide an understanding of the indirect impacts on climate change caused by the undertaking’s consumed energy whether externally purchased or acquired
         -(c) gross Scope 3 GHG emissions as required by paragraph 44 (c) is to provide an understanding of the GHG emissions that occur in the undertaking’s upstream and downstream value chain beyond its Scope 1 and 2 GHG emissions. For many undertakings, Scope 3 GHG emissions may be the main component of their GHG inventory and are an important driver of the undertaking’s transition risks .
         -(d) total GHG emissions as required by paragraph 44 (d) is to provide an overall understanding of the undertaking’s GHG emissions and whether they occur from its own operations or the usptream and downstream value chain. This disclosure is a prerequisite for measuring progress towards reducing GHG emissions in accordance with the undertaking’s climate-related targets and EU policy goals.
       The information from this Disclosure Requirement is also needed to understand the undertaking’s climate-related transition risks.
   """,
   'E1-6_46' : """
      - **Point 46:** When disclosing the information on GHG emissions required under paragraph 44, the undertaking shall refer to ESRS 1 paragraphs from 62 to 67. In principle, the data on GHG emissions of its associates or joint ventures that are part of the undertaking’s upstream and downstream value chain (ESRS 1 Paragraph 67) are not limited to the share of equity held. For its associates, joint ventures, unconsolidated subsidiaries (investment entities) and contractual arrangements that are joint arrangements not structured through an entity (i.e., jointly controlled operations and assets), the undertaking shall include the GHG emissions in accordance with the extent of the undertaking’s operational control over them.
   """,
   'E1-6_47' : """
      - **Point 47:** In case of significant changes in the definition of what constitutes the reporting undertaking and its upstream and downstream value chain , the undertaking shall disclose these changes and explain their effect on the year-to-year comparability of its reported GHG emissions (i.e., the effect on the comparability of current versus previous reporting period GHG emissions).
   """,
   'E1-6_48' : """
      - **Point 48:** The disclosure on gross Scope 1 GHG emissions required by paragraph 44 (a) shall include:
      Energy intensity based on net revenue
         -(a) the gross Scope 1 GHG emissions in metric tonnes of CO2eq; and
         -(b) the percentage of Scope 1 GHG emissions from regulated emission trading schemes.
   """,
   'E1-6_49' : """
      - **Point 49:** The disclosure on gross Scope 2 GHG emissions required by paragraph 44 (b) shall include:
         -(a) the gross location-based Scope 2 GHG emissions in metric tonnes of CO2eq; and
         -(b) the gross market-based Scope 2 GHG emissions in metric tonnes of CO2eq.
   """,
   'E1-6_50' : """
      - **Point 50:** For Scope 1 and Scope 2 emissions disclosed as required by paragraphs 44 (a) and (b) the undertaking shall disaggregate the information, separately disclosing emissions from:
         -(a) the consolidated accounting group (the parent and subsidiaries); and
         -(b) investees such as associates, joint ventures, or unconsolidated subsidiaries that are not fully consolidated in the financial statements of the consolidated accounting group, as well as contractual arrangements that are joint arrangements not structured through an entity (i.e., jointly controlled operations and assets), for which it has operational control.
   """,
   'E1-6_51' : """
      - **Point 51:** The disclosure of gross Scope 3 GHG emissions required by paragraph 44 (c) shall include GHG emissions in metric tonnes of CO2eq from each significant Scope 3 category (i.e. each Scope 3 category that is a priority for the undertaking) .
   """,
   'E1-6_52' : """
      - **Point 52:** The disclosure of total GHG emissions required by paragraph 44 (d) shall be the sum of Scope 1, 2 and 3 GHG emissions required by paragraphs 44 (a) to (c). The total GHG emissions shall be disclosed with a disaggregation that makes a distinction of:
         -(a) the total GHG emissions derived from the underlying Scope 2 GHG emissions being measured using the location-based method; and
         -(b) the total GHG emissions derived from the underlying Scope 2 GHG emissions being measured using the market-based method.
   """,
   'E1-6_53' : """
   GHG Intensity based on net revenue 
      - **Point 53:** The undertaking shall disclose its GHG emissions intensity (total GHG emissions per net revenue).
   """,
   'E1-6_54' : """
      - **Point 54:** The disclosure on GHG intensity required by paragraph 53 shall provide the total GHG emissions in metric tonnes of CO2eq (required by paragraph 44 (d)) per net revenue.
   """,
   'E1-6_55' : """
      - **Point 55:** The undertaking shall disclose the reconciliation to the relevant line item or notes in the financial statements of the net revenue amounts (the denominator in the calculation of the GHG emissions intensity required by paragraph 53).
   """,
   'E1-7_56' : """
      - **Point 56:** The undertaking shall disclose:
         -(a) GHG removals and storage in metric tonnes of CO2eq resulting from projects it may have developed in its own operations, or contributed to in its upstream and downstream value chain; and
         -(b) the amount of GHG emission reductions or removals from climate change mitigation projects outside its value chain it has financed or intends to finance through any purchase of carbon credits.
   """,
   'E1-7_57' : """
      - **Point 57:** The objective of this Disclosure Requirement is:
         -(a) to provide an understanding of the undertaking’s actions to permanently remove or actively support the removal of GHG from the atmosphere, potentially for achieving net-zero targets (as stated in paragraph 60).
         -(b) to provide an understanding of the extent and quality of carbon credits the undertaking has purchased or intends to purchase from the voluntary market, potentially for supporting its GHG neutrality claims (as stated in paragraph 61).
   """,
   'E1-7_58' : """
      - **Point 58:** The disclosure on GHG removals and storage required by paragraph 56 (a) shall include, if applicable:
         -(a) the total amount of GHG removals and storage in metric tonnes of CO2eq disaggregated and separately disclosed for the amount related to the undertaking’s own operations and its upstream and downstream value chain, and broken down by removal activity; and
         -(b) the calculation assumptions, methodologies and frameworks applied by the undertaking.
   """,
   'E1-7_59' : """
      - **Point 59:** The disclosure on carbon credits required by paragraph 56 (b) shall include, if applicable:
         -(a) the total amount of carbon credits outside the undertaking’s value chain in metric tonnes of CO2eq that are verified against recognised quality standards and cancelled in the reporting period; and
         -(b) the total amount of carbon credits outside the undertaking’s value chain in metric tonnes of CO2eq planned to be cancelled in the future and whether they are based on existing contractual agreements or not.
   """,
   'E1-7_60' : """
      - **Point 60:** In the case where the undertaking discloses a net-zero target in addition to the gross GHG emission reduction targets in accordance with Disclosure Requirement E1-4, paragraph 30, it shall explain the scope, methodologies and frameworks applied and how the residual GHG emissions (after approximately 90-95 percent of GHG emission reduction with the possibility for justified sectoral variations in line with a recognised sectoral decarbonisation pathway) are intended to be neutralised by, for example, GHG removals in its own operations and upstream and downstream value chain.
   """,
   'E1-7_61' : """
      - **Point 61:** In the case where the undertaking may have made public claims of GHG neutrality that involve the use of carbon credits , it shall explain:
         -(a) whether and how these claims are accompanied by GHG emission reduction targets as required by Disclosure requirement ESRS E1-4;
         -(b) whether and how these claims and the reliance on carbon credits neither impede nor reduce the achievement of its GHG emission reduction targets ( 47 ) , or, if applicable, its net zero target; and
         -(c) the credibility and integrity of the carbon credits used, including by reference to recognised quality standards.
   """,
   'E1-8_62' : """
      - **Point 62:** The undertaking shall disclose whether it applies internal carbon pricing schemes , and if so, how they support its decision making and incentivise the implementation of climate-related policies and targets .
   """,
   'E1-8_63' : """
      - **Point 63:** The information required in paragraph 62 shall include:
         -(a) 	the type of internal carbon pricing scheme, for example, the shadow prices applied for CapEX or research and development (R&D) investment decision making, internal carbon fees or internal carbon funds;
         -(b) the specific scope of application of the carbon pricing schemes (activities, geographies, entities, etc.);
         -(c) the carbon prices applied according to the type of scheme and critical assumptions made to determine the prices, including the source of the applied carbon prices and why these are deemed relevant for their chosen application. The undertaking may disclose the calculation methodology of the carbon prices including the extent to which these have been set using scientific guidance and how their future development is related to science-based carbon pricing trajectories; and
         -(d) the current year approximate gross GHG emission volumes by Scopes 1, 2 and, where applicable, Scope 3 in metric tonnes of CO2eq covered by these schemes, as well as their share of the undertaking’s overall GHG emissions for each respective Scope.
   """,
   'E1-9_64' : """
      - **Point 64:** The undertaking shall disclose its:
         -(a) anticipated financial effects from material physical risks ;
         -(b) anticipated financial effects from material transition risks ; and
         -(c) potential to benefit from material climate-related opportunities.
   """,
   'E1-9_65' : """
      - **Point 65:** The information required by paragraph 64 is in addition to the information on current financial effects required under ESRS 2 SBM-3 para 48 (d). The objective of this Disclosure Requirement related to:
         -(a) 	anticipated financial effects due to material physical risk s and transition risks is to provide an understanding of how these risks have (or could reasonably be expected to have) a material influence on the undertaking’s financial position, financial performance and cash flows, over the short-, medium- and long- term. The results of scenario analysis used to conduct resilience analysis as required under paragraphs AR 10 to AR 13 should inform the assessment of anticipated financial effects from material physical and transition risks.
         -(b) potential to pursue material climate-related opportunities is to enable an understanding of how the undertaking may financially benefit from material climate- related opportunities. This disclosure is complementary to the key performance indicators to be disclosed in accordance with Commission Delegated Regulation (EU) 2021/2178.
   """,
   'E1-9_66' : """
      - **Point 66:** The disclosure of anticipated financial effects from material physical risks required by paragraph 64 (a) shall include:
         -(a) 	the monetary amount and proportion (percentage) of assets at material physical risk over the short-, medium- and long-term before considering climate change adaptation actions ; with the monetary amounts of these assets disaggregated by acute and chronic physical risk;
         -(b) the proportion of assets at material physical risk addressed by the climate change adaptation actions ;
         -(c) the location of significant assets at material physical risk; and
         -(d) the monetary amount and proportion (percentage) of net revenue from its business activities at material physical risk over the short-, medium- and long-term.
   """,
   'E1-9_67' : """
      - **Point 67:** The disclosure of anticipated financial effects from material transition risks required by paragraph 64 (b) shall include:
         -(a) 	the monetary amount and proportion (percentage) of assets at material transition risk over the short-, medium- and long-term before considering climate mitigation actions ;
         -(b) the proportion of assets at material transition risk addressed by the climate change mitigation actions ;
         -(c) a breakdown of the carrying value of the undertaking’s real estate assets by energy-efficiency classes;
         -(d) liabilities that may have to be recognised in financial statements over the short-, medium- and long-term; and
         -(e) the monetary amount and proportion (percentage) of net revenue from its business activities at material transition risk over the short-, medium- and long-term including, where relevant, the net revenue from the undertaking’s customers operating in coal, oil and gas-related activities.
   """,
   'E1-9_68' : """
      - **Point 68:** The undertaking shall disclose reconciliations to the relevant line items or notes in the financial statements of the following:
         -(a) significant amounts of the assets and net revenue at material physical risk (as required by paragraph 66);
         -(b) significant amounts of the assets, liabilities, and net revenue at material transition risk (as required by paragraph 67).
   """,
   'E1-9_69' : """
      - **Point 69:** For the disclosure of the potential to pursue climate-related opportunities required by paragraph 64 (c) the undertaking shall consider ( 52 ) :
         -(a) its expected cost savings from climate change mitigation and adaptation actions ; and
         -(b) the potential market size or expected changes to net revenue from low-carbon products and services or adaptation solutions to which the undertaking has or may have access.
   """,
   'E1-9_70'  :"""
      - **Point 70:** A quantification of the financial effects that arise from opportunities is not required if such a disclosure does not meet the qualitative characteristics of useful information included under ESRS 1 Appendix B Qualitative characteristics of information .
   """,

   'E2-1_12': """
   - **Point 12:** The undertaking shall describe its policies adopted to manage its material impacts, risks and opportunities related to pollution prevention and control.
""",
'E2-1_13': """
   - **Point 13:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of material pollution-related impacts, risks and opportunities.
""",
'E2-1_14': """
   - **Point 14:** The disclosure required by paragraph 12 shall contain the information on the policies the undertaking has in place to manage its material impacts, risks and opportunities related to pollution in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters .
""",
'E2-1_15': """
   - **Point 15:** The undertaking shall indicate, with regard to its own operations and its upstream and downstream value chain , whether and how its policies address the following areas where material:
      -(a) mitigating negative impacts related to pollution of air, water and soil including prevention and control;
      -(b) substituting and minimising the use of substances of concern , and phasing out substances of very high concern , in particular for non-essential societal use and in consumer products; and
      -(c) avoiding incidents and emergency situations, and if and when they occur, controlling and limiting their impact on people and the environment.
""",
'E2-2_16': """
   - **Point 16:** Disclosure of pollution-related actions and the resources allocated to their implementation.
""",
'E2-2_17': """
   - **Point 17:** Explanation of key actions taken and planned to achieve pollution-related policy objectives and targets.
""",
'E2-2_18': """
   - **Point 18:** Description of action plans and resources, as prescribed in ESRS 2 MDR-A, related to material sustainability matters.
""",
'E2-2_19': """
   - **Point 19:** Alignment of actions and resources with the mitigation hierarchy:
     - (a) Avoid pollution (e.g., phase-out of harmful materials).
     - (b) Reduce pollution (e.g., meeting Best Available Techniques or DNSH criteria under the EU Taxonomy Regulation).
     - (c) Restore or regenerate ecosystems impacted by pollution.
""",
'E2-3_20': """
   - **Point 20:** The undertaking shall disclose the pollution-related targets it has set.
""",
'E2-3_21': """
   - **Point 21:** The objective of this Disclosure Requirement is to enable an understanding of the targets the undertaking has set to support its pollution  -related policies and to address its material pollution-related impacts, risks and opportunities.
""",
'E2-3_22': """
   - **Point 22:** The description of targets shall contain the information requirements defined in ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets.
""",
'E2-3_23': """
   - **Point 23:** The disclosure required by paragraph 20 shall indicate whether and how its targets relate to the prevention and control of:
     - (a) air pollutants and respective specific loads ;
     - (b) emissions to water and respective specific loads;
     - (c) pollution to soil and respective specific loads;
     - (d) substances of concern and substances of very high concern.
""",
'E2-3_24': """
   - **Point 24:** In addition to ESRS 2 MDR-T, the undertaking may specify whether ecological thresholds (e.g., the biosphere integrity , stratospheric ozone-depletion, atmospheric aerosol loading, soil depletion, ocean acidification) and entity-specific allocations were taken into consideration when setting targets. If so, the undertaking may specify:
     - (a) the ecological thresholds identified, and the methodology used to identify such thresholds;
     - (b) whether or not the thresholds are entity-specific and if so, how they were determined;
     - (c) how responsibility for respecting identified ecological thresholds is allocated in the undertaking.
""",
'E2-3_25': """
   - **Point 25:** The undertaking shall specify as part of the contextual information, whether the targets that it has set and presented are mandatory (required by legislation) or voluntary.
""",
'E2-4_26': """
   - **Point 26:** The undertaking shall disclose the pollutants that it emits through its own operations, as well as the microplastics it generates or uses..
""",
'E2-4_27': """
   - **Point 27:** The objective of this Disclosure Requirement is to provide an understanding of the emissions that the undertaking generates to air, water and soil in its own operations, and of its generation and use of microplastics.
""",
'E2-4_28': """
   - **Point 28:** The undertaking shall disclose the amounts of:
     - (a) 	each pollutant listed in Annex II of Regulation (EC) No 166/2006 of the European Parliament and of the Council ( 64 ) (European Pollutant Release and Transfer Register “E-PRTR Regulation”)emitted to air, water and soil, with the exception of emissions of GHGs which are disclosed in accordance with ESRS E1 Climate Change;
     - (b) microplastics generated or used by the undertaking.
""",
'E2-4_29': """
   - **Point 29:** The amounts referred in paragraph 28 shall be consolidated amounts including the emissions from those facilities over which the undertaking has financial control and those over which it has operational control. The consolidation shall include only the emissions from facilities for which the applicable threshold value specified in Annex II of Regulation (EC) No 166/2006 is exceeded.
""",
'E2-4_30': """
   - **Point 30:** The undertaking shall put its disclosure into context and describe:.   
     - (a) the changes over time,
     - (b) the measurement methodologies;
     - (c) the process(es) to collect data for pollution -related accounting and reporting, including the type of data needed and the information sources.
""",
'E2-4_31': """
   - **Point 31:** When an inferior methodology compared to direct measurement of emissions is chosen to quantify emissions, the reasons for choosing this inferior methodology shall be outlined by the undertaking. If the undertaking uses estimates, it shall disclose the standard, sectoral study or sources which form the basis of its estimates, as well as the possible degree of uncertainty and the range of estimates reflecting the measurement uncertainty.
""",
'E2-5_32': """
   - **Point 32:** The undertaking shall disclose information on the production, use, distribution, commercialisation and import/export of substances of concern and substances of very high concern, on their own, in mixtures or in articles.
""",
'E2-5_33': """
   - **Point 33:** The objective of this Disclosure Requirement is to enable an understanding of the impact of the undertaking on health and the environment through substances of concern and through substances of very high concern on their own. It is also to enable an understanding of the undertaking’s material risks and opportunities , including exposure to those substances and risks arising from changes in regulations.
""",
'E2-5_34': """
   - **Point 34:** The disclosure required by paragraph 32 shall include the total amounts of substances of concern that are generated or used during the production or that are procured, and the total amounts of substances of concern that leave its facilities as emissions, as products, or as part of products or services split into main hazard classes of substances of concern.
""",
'E2-5_35': """
   - **Point 35:** The undertaking shall present separately the information for substances of very high concern.
""",
'E2-6_36': """
   - **Point 36:** The undertaking shall disclose the anticipated financial effects of material pollution-related risks and opportunities.
""",
'E2-6_37': """
   - **Point 37:** The information required by paragraph 36 is in addition to the information on current financial effects on the undertaking’s, financial position, financial performance and cash flows for the reporting period required under ESRS 2 SBM-3 para 48 (d).
""",
'E2-6_38': """
   - **Point 38:** The objective of this Disclosure Requirement is to provide an understanding of:
     - (a) anticipated financial effects due to material risks arising from pollution -related impacts and dependencies and how those risks have (or could reasonably be expected to have) a material influence on the undertaking’s financial position financial performance and cash flows, over the short-, medium- and long-term.
     - (b) anticipated financial effects due to material opportunities related to pollution prevention and control.
""",
'E2-6_39': """
   - **Point 39:** The disclosure shall include:
     - (a) a quantification of the anticipated financial effects in monetary terms before considering pollution-related actions, or where not possible without undue cost or effort, qualitative information. For financial effects arising from opportunities , a quantification is not required if it would result in disclosure that does not meet the qualitative characteristics of information (see ESRS 1 Appendix B Qualitative characteristics of information );
     - (b) a description of the effects considered, the related impacts and the time horizons in which they are likely to materialise;
     - (c) the critical assumptions used to quantify the anticipated financial effects , as well as the sources and level of uncertainty of those assumptions.
""",
'E2-6_40': """
   - **Point 40:** The information provided under paragraph 39(a) shall include:   
     - (a) the share of net revenue made with products and services that are or that contain substances of concern , and the share of net revenue made with products and services that are or that contain substances of very high concern ;,
     - (b) the operating and capital expenditures incurred in the reporting period in conjunction with major incidents and deposits ;
     - (c) the provisions for environmental protection and remediation costs, e.g., for rehabilitating contaminated sites , recultivating landfills, removal of environmental contamination at existing production or storage sites and similar measures.
""",
'E2-6_41': """
   - **Point 41:** The undertaking shall disclose any relevant contextual information including a description of material incidents and deposits whereby pollution had negative impacts on the environment and/or is expected to have negative effects on the undertaking’s financial cash flows, financial position and financial performance with short-, medium- and long-term time horizons.
""",
'E3-1_9': """
   - **Point 9:** The undertaking shall describe its policies adopted to manage its material impacts, risks and opportunities related to water and marine resources.
""",
'E3-1_10': """
   - **Point 10:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of its material water and marine resources -related impacts, risks and opportunities.
""",
'E3-1_11': """
   - **Point 11:** The disclosure required by paragraph 9 shall contain the information on the policies the undertaking has in place to manage its material impacts, risks and opportunities related to water and marine resources in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters.
""",
'E3-1_12': """
   - **Point 12:** The undertaking shall indicate whether and how its policies address the following matters where material:
     - (a) water management including:
        i.   the use and sourcing of water and marine resources in its own operations;
        ii.  water treatment as a step towards more sustainable sourcing of water; and
        iii. the prevention and abatement of water pollution resulting from its activities.
     - (b) product and service design in view of addressing water-related issues and the preservation of marine resources;
     - (c) commitment to reduce material water consumption in areas at water risk in its own operations and along the upstream and downstream value chain.
""",
'E3-1_13': """
   - **Point 13:** If at least one of the sites of the undertaking is located in an area of high-water stress and it is not covered by a policy , the undertaking shall state this to be the case and provide reasons for not having adopted such a policy. The undertaking may disclose a timeframe in which it aims to adopt such a policy. 
""",
'E3-1_14': """
   - **Point 14:** The undertaking shall specify whether it has adopted policies or practices related to sustainable oceans and seas.
""",
'E3-2_15': """
   - **Point 15:** The undertaking shall disclose its water and marine resources-related actions and the resources allocated to their implementation.
""",
'E3-2_16': """
   - **Point 16:** The objective of this Disclosure Requirement is to enable an understanding of the key actions taken and planned to achieve the water and marine resources -related policy objectives and targets.
""",
'E3-2_17': """
   - **Point 17:** The description of the actions and resources shall follow the principles defined in ESRS 2 MDR-A Actions and resources in relation to material sustainability matters . In addition to ESRS 2 MDR-A, the undertaking may specify to which layer in the mitigation hierarchy an action
""",
'E3-2_18': """
   - **Point 18:** Resources can be allocated to:
     - (a) avoid the use of water and marine resources ;
     - (b) reduce the use of water and marine resources such as through efficiency measures;
     - (c) reclaiming and reuse of water;
     - (d) restoration and regeneration of aquatic ecosystem and water bodies.
""",
'E3-2_19': """
   - **Point 19:** The undertaking shall specify actions and resources in relation to areas at water risk , including areas of high-water stress. 
""",
'E3-3_20': """
   - **Point 20:** The undertaking shall disclose the water and marine resources-related targets it has set.
""",
'E3-3_21': """
   - **Point 21:** The objective of this Disclosure Requirement is to enable an understanding of the targets the undertaking has adopted to support its water and marine resources-related policies and address its material water and marine resources-related impacts, risks and opportunities.
""",
'E3-3_22': """
   - **Point 22:** The description of the targets shall contain the information requirements defined in ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets.
""",
'E3-3_23': """
   - **Point 23:** The disclosure required by paragraph 20 shall indicate whether and how its targets relate to:
     - (a) the management of material impacts, risks and opportunities related to areas at water risk , including improvement of the water quality;
     - (b) the responsible management of marine resources impacts, risks and opportunities including the nature and quantity of marine resources-related commodities (such as gravels, deep-sea minerals, seafood) used by the undertaking;
     - (c) the reduction of water consumption , including an explanation of how those targets relate to areas at water risk, including areas of high water-stress.
""",
'E3-3_24': """
   - **Point 24:** In addition to ESRS 2 MDR-T, the undertaking may specify whether ecological thresholds and entity-specific allocations were taken into consideration when setting targets . If so, the undertaking may specify:
     - (a) the ecological thresholds identified, and the methodology used to identify such thresholds;
     - (b) whether or not the thresholds are entity-specific and if so, how they were determined;
     - (c) how responsibility for respecting identified ecological thresholds is allocated in the undertaking.
""",
'E3-3_25': """
   - **Point 25:** The undertaking shall specify as part of the contextual information, whether the targets it has set and presented are mandatory (required by legislation) or voluntary. 
""",
'E3-4_26': """
   - **Point 26:** The undertaking shall disclose information on its water consumption performance related to its material impacts, risks and opportunities.
""",
'E3-4_27': """
   - **Point 27:** The objective of this Disclosure Requirement is to provide an understanding of the undertaking’s water consumption and any progress by the undertaking in relation to its targets.
""",
'E3-4_28': """
   - **Point 28:** The disclosure required by paragraph 26 relates to own operations and shall include:
     - (a) total water consumption in m3;
     - (b) total water consumption in m3 in areas at water risk, including areas of high-water stress ;
     - (c) total water recycled and reused in m3;
     - (d) total water stored and changes in storage in m3;
     - (e) any contextual information necessary regarding points (a) to (d), including the water basins’ water quality and quantity, how the data have been compiled, such as any standards, methodologies, and assumptions used, including whether the information is calculated, estimated, modelled, or sourced from direct measurements, and the approach taken for this, such as the use of any sector-specific factors.
""",
'E3-4_29': """
   - **Point 29:** The undertaking shall provide information on its water intensity : total water consumption in its own operations in m3 per million EUR net revenue
""",
'E3-5_30': """
   - **Point 30:** The undertaking shall disclose the anticipated financial effects of material water and marine resources-related risks and opportunities.
""",
'E3-5_31': """
   - **Point 31:** The information required by paragraph 30 is in addition to the information on current financial effects on the entity’s financial position, financial performance and cash flows for the reporting period required under ESRS 2 SBM-3 para 48 (d).
""",
'E3-5_32': """
   - **Point 32:** The objective of this Disclosure Requirement is to provide an understanding of:
     - (a) anticipated financial effects due to material risks arising from water and marine resources -related impacts and dependencies and how these risks have (or could reasonably be expected to have) a material influence on the undertaking’s financial position, financial performance and cash flows, over the short-, medium- and long-term;
     - (b) anticipated financial effects due to material opportunities related to water and marine resources.
""",
'E3-5_33': """
   - **Point 33:** The disclosure shall include:
     - (c) a quantification of the anticipated financial effects in monetary terms before considering water and marine resources-related actions or where not possible without undue cost or effort, qualitative information. For financial effects arising from opportunities, a quantification is not required if it would result in disclosure that does not meet the qualitative characteristics of information (see ESRS 1 Appendix B Qualitative characteristics of information );
     - (d) a description of the effects considered, the impacts and dependencies to which they relate, and the time horizons in which they are likely to materialise;
     - (e) the critical assumptions used to quantify the anticipated financial effects, as well as the sources and level of uncertainty of those assumptions.
""",
'E4-1_11': """
   - **Point 11:** The undertaking shall disclose how its biodiversity and ecosystem impacts, dependencies, risks and opportunities originate from and trigger adaptation of its strategy and business model..
""",
'E4-1_12': """
   - **Point 12:** The objective of this Disclosure Requirement is to enable an understanding of the resilience of the undertaking’s strategy and business model in relation to biodiversity and ecosystems , and of the compatibility of the undertaking’s strategy and business model with regard to relevant local, national and global public policy targets related to biodiversity and ecosystems.
""",
'E4-1_13': """
   - **Point 13:** The undertaking shall describe the resilience of its strategy and business model in relation to biodiversity and ecosystems . The description shall include:
     - (a) an assessment of the resilience of the current business model and strategy to biodiversity and ecosystems-related physical, transition and systemic risks;
     - (b) the scope of the resilience analysis in relation to the undertaking’s own operations and its upstream and downstream value chain and in relation to the risks considered in that analysis;
     - (c) the key assumptions made;
     - (d) the time horizons used;
     - (e) the results of the resilience analysis;
     - (f) the involvement of stakeholders, including, where appropriate, holders of indigenous and local knowledge.
""",
'E4-1_14': """
   - **Point 14:** If information specified in this disclosure requirement is disclosed by the undertaking as part of the information required under ESRS 2 SBM-3, the undertaking may refer to the information it has disclosed under ESRS 2 SBM-3.
""",
'E4-1_15': """
   - **Point 15:** The undertaking may disclose its transition plan to improve and, ultimately, achieve alignment of its business model and strategy with the vision of the Kunming-Montreal Global Biodiversity Framework and its relevant goals and targets, the EU Biodiversity Strategy for 2030, and with respecting planetary boundaries related to biosphere integrity and land-system change .
""",
'E4-1_16': """
Disclosure Requirement SBM 3 – Material impacts, risks and opportunities and their interaction with strategy and business model

   - **Point 16:** The undertaking shall disclose:
     - (a) a list of material sites in its own operations, including sites under its operational control, based on the results of paragraph 17(a). The undertaking shall disclose these locations by:
            i. specifying the activities negatively affecting biodiversity sensitive areas ( 80 ) ;
            ii. providing a breakdown of sites according to the impacts and dependencies identified, and to the ecological status of the areas (with reference to the specific ecosystem baseline level) where they are located; and
            iii.specifying the biodiversity-sensitive areas impacted, for users to be able to determine the location and the responsible competent authority with regards to the activities specified in paragraph 16(a) i.
     - (b) whether it has identified material negative impacts with regards to land degradation , desertification or soil sealing ( 81 ) ;
     - (c) whether it has operations that affect threatened species.
""",
'E4-2_20': """
   - **Point 20:** The undertaking shall describe its adopted policies to manage its material impacts, risks, dependencies, and opportunities that are related to biodiversity and ecosystems.
""",
'E4-2_21': """
   - **Point 21:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of its material biodiversity and ecosystem - related impacts , dependencies , risks and opportunities .
""",
'E4-2_22': """
   - **Point 22:** The disclosure required by paragraph 20 shall contain the information on the policies the undertaking has in place to manage its material impacts, risks, dependencies and opportunities related to biodiversity and ecosystems in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters ).
""",
'E4-2_23': """
    - **Point 23:** In addition to the provisions of ESRS 2 MDR-P the undertaking shall describe whether and how its biodiversity and ecosystems -related policies :
     - (a) relate to the matters specified in ESRS E4 AR 4;
     - (b) relate to its material biodiversity and ecosystems-related impacts;
     - (c) relate to material dependencies and material physical and transition risks and opportunities;
     - (d) support traceability of products, components and raw materials with material actual or potential impacts on biodiversity and ecosystems along the value chain ;
     - (e) address production, sourcing or consumption from ecosystems that are managed to maintain or enhance conditions for biodiversity, as demonstrated by regular monitoring and reporting of biodiversity status and gains or losses;
     - (f) address social consequences of biodiversity and ecosystems-related impacts.
""",
'E4-2_24': """
    - **Point 24:** The undertaking shall specifically disclose whether it has adopted:
     - (a) biodiversity and ecosystem protection policy covering operational sites owned, leased, or managed in or near a biodiversity sensitive area;
     - (b) sustainable land / agriculture practices or policies
     - (c) sustainable oceans / seas practices or policies
     - (d) policies to address deforestation
""",
'E4-3_25': """
   - **Point 25:** The undertaking shall disclose its biodiversity and ecosystems-related actions and the resources allocated to their implementation.
""",
'E4-3_26': """
   - **Point 26:** The objective of this Disclosure Requirement is to enable an understanding of the key actions taken and planned that significantly contribute to the achievement of biodiversity and ecosystems -related policy objectives and targets .
""",
'E4-3_27': """
   - **Point 27:** The description of key actions and resources shall follow the mandatory content defined in ESRS 2 MDR-A Actions and resources in relation to material sustainability matters .
""",
'E4-3_28': """
    - **Point 28:** In addition, the undertaking :
     - (a) 	may disclose how it has applied the mitigation hierarchy with regard to its actions (avoidance, minimisation, restoration/rehabilitation, and compensation or offsets);
     - (b) shall disclose whether it used biodiversity offsets in its action plans. If the actions contain biodiversity offsets, the undertaking shall include the following information:
            i. the aim of the offset and key performance indicators used;;
            ii. the financing effects (direct and indirect costs) of biodiversity offsets in monetary terms;
            iii.a description of offsets including area, type, the quality criteria applied and the standards that the biodiversity offsets comply with;
     - (c) shall describe whether and how it has incorporated local and indigenous knowledge and nature- based solutions into biodiversity and ecosystems -related actions.
""",
'E4-4_29': """
   - **Point 29:** The undertaking shall disclose the biodiversity and ecosystem-related targets it has set.
""",
'E4-4_30': """
   - **Point 30:** The objective of this Disclosure Requirement is to allow an understanding of the targets the undertaking has adopted to support its biodiversity and ecosystems policies and address its material related impacts , dependencies , risks and opportunities .
""",
'E4-4_31': """
   - **Point 31:** The description of the targets shall follow the mandatory content defined in ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets.
""",
'E4-4_32': """
   - **Point 32:** The disclosure required by paragraph 29 shall include the following information:
     - (a) 	whether ecological thresholds and allocations of impacts to the undertaking were applied when setting targets. If so, the undertaking shall specify:
            i.  the ecological thresholds identified and the methodology used to identify such thresholds;
            ii. whether or not the thresholds are entity-specific and if so, how they were determined; 
            iii. how responsibility for respecting identified ecological thresholds is allocated in the undertaking;
     - (b) whether the targets are informed by, and/or aligned with the Kunming-Montreal Global Biodiversity Framework, relevant aspects of the EU Biodiversity Strategy for 2030 and other biodiversity and ecosystem -related national policies and legislation;
     - (c) how the targets relate to the biodiversity and ecosystem impacts, dependencies, risks and opportunities identified by the undertaking in relation to its own operations and its upstream and downstream value chain;
     - (d) the geographical scope of the targets, if relevant;
     - (e) whether or not the undertaking used biodiversity offsets in setting its targets;
     - (f) to which of the layers of the mitigation hierarchy the target can be allocated (i.e., avoidance, minimisation, restoration and rehabilitation, compensation or offsets).;
""",
'E4-5_33': """
   - **Point 33:** The undertaking shall report metrics related to its material impacts on biodiversity and ecosystems .
""",
'E4-5_34': """
   - **Point 34:** The objective of this Disclosure Requirement is to enable an understanding of the performance of the undertaking against impacts identified as material in the materiality assessment on biodiversity and ecosystems change.
""",
'E4-5_35': """
   - **Point 35:** If the undertaking identified sites located in or near biodiversity-sensitive areas that it is negatively affecting (see paragraph 19(a)), the undertaking shall disclose the number and area (in hectares) of sites owned, leased or managed in or near these protected areas or key biodiversity areas.
""",
'E4-5_36': """
   - **Point 36:** If the undertaking has identified material impacts with regards to land-use change, or impacts on the extent and condition of ecosystems , it may also disclose their land-use based on a Life Cycle Assessment.
""",
'E4-5_37': """
   - **Point 37:** For datapoints specified in paragraphs 38 to 41, the undertaking shall consider its own operations.
""",
'E4-5_38': """
   - **Point 38:** If the undertaking has concluded that it directly contributes to the impact drivers of land-use change , freshwater -use change and/or sea-use change, it shall report relevant metrics. The undertaking may disclose metrics that measure:
     - (a) the conversion over time (e.g. 1 or 5 years) of land cover (e.g. deforestation or mining);
     - (b) changes over time (e.g. 1 or 5 years) in the management of the ecosystem (e.g., through the intensification of agricultural management, or the application of better management practices or forestry harvesting);
     - (c) changes in the spatial configuration of the landscape (e.g. fragmentation of habitats, changes in ecosystem connectivity);
     - (d) changes in ecosystem structural connectivity (e.g. habitat permeability based on physical features and arrangements of habitat patches);
     - (e) the functional connectivity (e.g. how well genes or individuals move through land, freshwater and seascape).
""",
'E4-5_39': """
   - **Point 39:** If the undertaking concluded that it directly contributes to the accidental or voluntary introduction of invasive alien species, the undertaking may disclose the metrics it uses to manage pathways of introduction and spread of invasive alien species and the risks posed by invasive alien species.
""",
'E4-5_40': """
   - **Point 40:** If the undertaking identified material impacts related to the state of species, the undertaking may report metrics it considers relevant. The undertaking may:
     - (a) refer to relevant disclosure requirements in ESRS E1, ESRS E2, ESRS E3, and ESRS E5;
     - (b) consider population size, range within specific ecosystems as well as extinction risk. These aspects provide insight on the health of a single species’ population and its relative resilience to human induced and naturally occurring change;
     - (c) disclose metrics that measure changes in the number of individuals of a species within a specific area;
     - (d) disclose metrics on species at extinction risk ( 87 ) that measure:
            i.  the threat status of species and how activities/pressures may affect the threat status; or 
            ii. changes in the relevant habitat for a threatened species as a proxy for the undertaking’s impact on the local population’s extinction risk. 
""",
'E4-5_41': """
   - **Point 41:** If the undertaking identified material impacts related to ecosystems, it may disclose:
     - (a) with regard to ecosystems extent, metrics that measure area coverage of a particular ecosystem without necessarily considering the quality of the area being assessed, such as habitat cover. For example, forest cover is a measure of the extent of a particular ecosystem type, without factoring in the condition of the ecosystem (e.g., provides the area without describing the species diversity within the forest).
     - (b) with regard to ecosystems condition:
            i.  metrics that measure the quality of ecosystems relative to a pre-determined reference state; 
            ii. metrics that measure multiple species within an ecosystem rather than the number of individuals within a single species within an ecosystem (for example: scientifically established species richness and abundance indicators that measure the development of (native) species composition within an ecosystem against the reference state at the beginning of the first reporting period as well as the targeted state outlined in the Kunming-Montreal Global Biodiversity Framework, or an aggregation of species’ conservation status if relevant); or 
            iii. metrics that reflect structural components of condition such as habitat connectivity (i.e., how linked habitats are to each other).
""",
'E4-6_42': """
   - **Point 42:** The undertaking shall disclose its anticipated financial effects of material biodiversity and ecosystem-related risks and opportunities
""",
'E4-6_43': """
   - **Point 43:** The information required by paragraph 42 is in addition to the information on current financial effects on the entity’s financial position, financial performance and cash flows for the reporting period required under ESRS 2 SBM-3 para 48 (d).
""",
'E4-6_44': """
   - **Point 44:** The objective of this Disclosure Requirement is to provide an understanding of:
     - (a) 	anticipated financial effects due to material risks arising from biodiversity- and ecosystem-related impacts and dependencies and how these risks have (or could reasonably be expected to have) a material influence on the undertaking’s financial position, financial performance and cash flows over the short-, medium- and long-term; and
     - (b) anticipated financial effects due to material opportunities related to biodiversity- and ecosystem.
""",
'E4-6_45': """
   - **Point 45:** The disclosure shall include:
     - (a) 	a quantification of the anticipated financial effects in monetary terms before considering biodiversity and ecosystems -related actions or where not possible without undue cost or effort, qualitative information. For financial effects arising from material opportunities, a quantification is not required if it would result in disclosure that does not meet the qualitative characteristics of information (see ESRS 1 Appendix B Qualitative characteristics of information ). The quantification of the anticipated financial effects in monetary terms may be a single amount or a range;
     - (b) a description of the effects considered, the impacts and dependencies to which they relate and the time horizons in which they are likely to materialise; and
     - (c) the critical assumptions used to quantify the anticipated financial effects as well as the sources and the level of uncertainty of those assumptions.
""",
'E5-1_12': """
   - **Point 12:** The undertaking shall describe its policies adopted to manage its material impacts, risks and opportunities related to resource use and circular economy.
""",
'E5-1_13': """
   - **Point 13:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of its material impacts, risks and opportunities related to resource use and circular economy.
""",
'E5-1_14': """
   - **Point 14:** The disclosure required by paragraph 12 shall contain the information on the policies the undertaking has in place to manage its material impacts, risks and opportunities related to resource use and circular economy in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters.
""",
'E5-1_15': """
   - **Point 15:** In the summary, the undertaking shall indicate whether and how its policies address the following matters where material:
     - (a) 	transitioning away from use of virgin resources, including relative increases in use of secondary (recycled) resources;
     - (b) sustainable sourcing and use of renewable resources.
""",
'E5-1_16': """
   - **Point 16:** Policies shall address material impacts, risks and opportunities in its own operations and along its upstream and downstream value chain.
""",
'E5-2_17': """
   - **Point 17:** The undertaking shall disclose its resource use and circular economy actions and the resources allocated to their implementation.
""",
'E5-2_18': """
   - **Point 18:** The objective of this Disclosure Requirement is to enable an understanding of the key actions taken and planned to achieve the resource use and circular economy-related policy objectives and targets .
""",
'E5-2_19': """
   - **Point 19:** The description of the resource use and circular economy-related actions and resources allocated shall follow the principles defined in ESRS 2 MDR-A Actions and resources in relation to material sustainability matters.
""",
'E5-2_20': """
   - **Point 20:** In addition to ESRS 2 MDR-A, the undertaking may specify whether and how an action and resources cover:
     - (a) higher levels of resource efficiency in use of technical and biological materials and water, particularly in relation to critical raw materials and rare earths as listed in the Raw Materials Information System;
     - (b) higher rates of use of secondary raw materials (recyclates);
     - (c) application of circular design, leading to increased product durability and optimisation of use, and higher rates of: Reuse, Repair, Refurbishing, Remanufacture, Repurposing and Recycling.
     - (d) application of circular business practices such as (i) value retention actions (maintenance, repair, refurbishing, remanufacturing, component harvesting, upgrading and reverse logistics, closed loop systems, second-hand retailing), (ii) value maximisation actions (product-service systems, collaborative and sharing economy business models), (iii) end-of-life actions ( recycling , upcycling, extended producer responsibility), and (iv) systems efficiency actions (industrial symbiosis);
     - (e) actions taken to prevent waste generation in the undertaking’s upstream and downstream value chain; and
     - (f) optimistation of waste management in line with the waste hierarchy.
""",
'E5-3_21': """
   - **Point 21:** The undertaking shall disclose the resource use and circular economy-related targets it has set.
""",
'E5-3_22': """
   - **Point 22:** The objective of this Disclosure Requirement is to enable an understanding of the targets the undertaking has adopted to support its resource use and circular economy policy and to address its material impacts, risks and opportunities.
""",
'E5-3_23': """
   - **Point 23:** The description of the targets shall contain the information requirements defined in ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets .
""",
'E5-3_24': """
   - **Point 24:** The disclosure required by paragraph 21 shall indicate whether and how the undertaking’s targets relate to resource inflows and resource outflows , including waste and products and materials, and, more specifically to:
     - (a) the increase of circular product design (including for instance design for durability , dismantling, reparability, recyclability etc);
     - (b) the increase of circular material use rate ;
     - (c) the minimisation of primary raw material;
     - (d) sustainable sourcing and use (in line with the cascading principle) of renewable resources;
     - (e) the waste management , including preparation for proper treatment; and
     - (f) other matters related to resource use or circular economy.
""",
'E5-3_25': """
   - **Point 25:** The undertaking shall specify to which layer of the waste hierarchy the target relates.
""",
'E5-3_26': """
   - **Point 26:** In addition to ESRS 2 MDR-T, the undertaking may specify whether ecological thresholds and entity-specific allocations were taken into consideration when setting targets . If so, the undertaking may specify:
     - (a) the ecological thresholds identified, and the methodology used to identify such thresholds;
     - (b) whether or not the thresholds are entity-specific and if so, how they were determined; and
     - (c) how responsibility for respecting identified ecological thresholds is allocated in the undertaking.
""",
'E5-3_27': """
   - **Point 27:** The undertaking shall specify as part of the contextual information, whether the targets it has set and presented are mandatory (required by legislation) or voluntary.
""",
'E5-4_28': """
   - **Point 28:** The undertaking shall disclose information on its resource inflows related to its material impacts, risks and opportunities.
""",
'E5-4_29': """
   - **Point 29:** The objective of this Disclosure Requirement is to enable an understanding of the resource use in the undertaking’s own operations and its upstream value chain.
""",
'E5-4_30': """
   - **Point 30:** The disclosure required by paragraph 28 shall include a description of its resource inflows where material: products (including packaging ) and materials (specifying critical raw materials and rare earths), water and property, plant and equipment used in the undertaking’s own operations and along its upstream value chain.
""",
'E5-4_31': """
   - **Point 31:** When an undertaking assesses that resource inflows is a material sustainability matter, it shall disclose the following information about the materials used to manufacture the undertaking’s products and services during the reporting period, in tonnes or kilogrammes:
     - (a) the overall total weight of products and technical and biological materials used during the reporting period;
     - (b) the percentage of biological materials (and biofuels used for non-energy purposes) used to manufacture the undertaking’s products and services (including packaging ) that is sustainably sourced, with the information on the certification scheme used and on the application of the cascading principle; and
     - (c) the weight in both absolute value and percentage, of secondary reused or recycled components, secondary intermediary products and secondary materials used to manufacture the undertaking’s products and services (including packaging).
""",
'E5-4_32': """
   - **Point 32:** 	The undertaking shall provide information on the methodologies used to calculate the data. It shall specify whether the data is sourced from direct measurement or estimations, and disclose the key assumptions used.
""",
'E5-5_33': """
   - **Point 33:** The undertaking shall disclose information on its resource outflows, including waste, related to its material impacts, risks and opportunities.
""",
'E5-5_34': """
   - **Point 34:** The objective of this Disclosure Requirement is to provide an understanding of:
     - (a) how the undertaking contributes to the circular economy by i) designing products and materials in line with circular economy principles and ii) increasing or maximising the extent to which products, materials and waste processing are recirculated in practice after first use; and
     - (b) the undertaking’s waste reduction and waste management strategy, the extent to which the undertaking knows how its pre-consumer waste is managed in its own activities.
""",
'E5-5_35': """
Products and materials

   - **Point 35:** The undertaking shall provide a description of the key products and materials that come out of the undertaking’s production process and that are designed along circular principles, including durability , reusability, repairability, disassembly, remanufacturing, refurbishment, recycling , recirculation by the biological cycle, or optimisation of the use of the product or material through other circular business models.
""",
'E5-5_36': """
   - **Point 36:** Undertakings for which outflows are material shall disclose:
     - (a) The expected durability of the products placed on the market by the undertaking, in relation to the industry average for each product group;
     - (b) The reparability of products, using an established rating system, where possible;
     - (c) The rates of recyclable content in products and their packaging .
""",
'E5-5_37': """
Waste
   - **Point 37:** The undertaking shall disclose the following information on its total amount of waste from its own operations, in tonnes or kilogrammes:
     - (a) the total amount of waste generated ;
     - (b) the total amount by weight diverted from disposal, with a breakdown between hazardous waste and non-hazardous waste and a breakdown by the following recovery operation types:
            i.  preparation for reuse; 
            ii. recycling ; and 
            iii. other recovery operations. 
     - (c) the amount by weight directed to disposal by waste treatment type and the total amount summing all three types, with a breakdown between hazardous waste and non-hazardous waste. The waste treatment types to be disclosed are:
            i.  incineration ; 
            ii. landfill; and
            iii. other disposal operations; 
     - (d) the total amount and percentage of non-recycled waste.""",
'E5-5_38': """
   - **Point 38:** 	When disclosing the composition of the waste , the undertaking shall specify:
     - (a) the waste streams relevant to its sector or activities (e.g. tailings for the undertaking in the mining sector, electronic waste for the undertaking in the consumer electronics sector, or food waste for the undertaking in the agriculture or in the hospitality sector); and;
     - (b) the materials that are present in the waste (e.g. biomass, metals, non-metallic minerals, plastics, textiles, critical raw materials and rare earths).
""",
'E5-5_39': """
   - **Point 39:** The undertaking shall also disclose the total amount of hazardous waste and radioactive waste generated by the undertaking, where radioactive waste is defined in Article 3(7) of Council Directive 2011/70/Euratom
""",
'E5-5_40': """
   - **Point 40:** The undertaking shall provide contextual information on the methodologies used to calculate the data and in particular the criteria and assumptions used to determine and classify products designed along circular principles under paragraph 35. It shall specify whether the data is sourced from direct measurement or estimations; and disclose the key assumptions used.
""",
'E5-6_41': """
   - **Point 41:** The undertaking shall disclose the anticipated financial effects of material risks and opportunities arising from resource use and circular economy-related impacts.
""",
'E5-6_42': """
   - **Point 42:** The information required by paragraph 41 is in addition the information on current financial effects on the entity’s financial position, financial performance and cash flows for the reporting period required under ESRS 2 SBM-3 para 48 (d). The objective of this Disclosure Requirement is to provide an understanding of:
     - (a) anticipated financial effects due to material risks arising from material resource use and circular economy -related impacts and dependencies and how these risks have or could reasonably be expected to have) a material influence on the undertaking’s financial position, financial performance performance, and cash flows over the short-, medium- and long-term; and
     - (b) anticipated financial effects due to material opportunities related to resource use and circular economy.
""",
'E5-6_43': """
   - **Point 43:** The disclosure shall include:
     - (a) a quantification of the anticipated financial effects in monetary terms before considering resource use and circular economy-related actions, or where not possible without undue cost or effort, qualitative information. For financial effects arising from material opportunities, a quantification is not required if it would result in disclosure that does not meet the qualitative characteristics of information (see ESRS 1 Appendix B Qualitative characteristics of information );
     - (b) a description of the effects considered, the impacts and dependencies to which they relate and the time horizons in which they are likely to materialise;
     - (c) the critical assumptions used to quantify the anticipated financial effects , as well as the sources and level of uncertainty of those assumptions.
""",
'S1-1_17': """
   - **Point 17:** The undertaking shall describe its policies adopted to manage its material impacts on its own workforce, as well as associated material risks and opportunities.
""",
'S1-1_18': """
   - **Point 18:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of material impacts on the undertaking’s own workforce specifically, as well as policies that cover material impacts, risks and opportunities related to its own workforce.
""",
'S1-1_19': """
   - **Point 19:** The disclosure required by paragraph 17 shall contain the information on the undertaking’s policies to manage its material impacts, risks and opportunities related to its own workforce in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters . In addition, the undertaking shall specify if such policies cover specific groups within its own workforce or all of its own workforce.
""",
'S1-1_20': """
   - **Point 20:** The undertaking shall describe its human rights policy commitments ( 96 ) that are relevant to its own workforce , including those processes and mechanisms to monitor compliance with the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work and the OECD Guidelines for Multinational Enterprises ( 97 ) . In its disclosure it shall focus on those matters that are material in relation to, as well as its general approach to:
     - (a) respect for the human rights, including labour rights, of people in its own workforce;
     - (b) engagement with people in its own workforce; and
     - (c) measures to provide and/or enable remedy for human rights impacts.
""",
'S1-1_21': """
   - **Point 21:** The undertaking shall disclose whether and how its policies with regard to its own workforce are aligned with relevant internationally recognised instruments, including the UN Guiding Principles on Business and Human Rights.
""",
'S1-1_22': """
   - **Point 22:** The undertaking shall state whether its policies in relation to its own workforce explicitly address trafficking in human beings ( 99 ) , forced labour or compulsory labour and child labour.
""",
'S1-1_23': """
   - **Point 23:** The undertaking shall state whether it has a workplace accident prevention policy or management system.
""",
'S1-1_24': """
   - **Point 24:** The undertaking shall disclose:
     - (a) whether it has specific policies aimed at the elimination of discrimination , including harassment , promoting equal opportunities and other ways to advance diversity and inclusion;
     - (b) whether the following grounds for discrimination are specifically covered in the policy : racial and ethnic origin, colour, sex, sexual orientation, gender identity, disability, age, religion, political opinion, national extraction or social origin, or other forms of discrimination covered by Union regulation and national law;
     - (c) whether the undertaking has specific policy commitments related to inclusion or positive action for people from groups at particular risk of vulnerability in its own workforce and, if so, what these commitments are; and
     - (d) whether and how these policies are implemented through specific procedures to ensure discrimination is prevented, mitigated and acted upon once detected, as well as to advance diversity and inclusion in general.
""",
'S1-2_25': """
   - **Point 25:** The undertaking shall disclose its general processes for engaging with people in its own workforce and workers' representatives about actual and potential impacts on its own workforce.
""",
'S1-2_26': """
   - **Point 26:** The objective of this Disclosure Requirement is to enable an understanding of how the undertaking engages, as part of its ongoing due diligence process, with people in its own workforce and workers' representatives about material, actual and potential, positive and/or negative impacts that do or are likely to affect them, and whether and how perspectives of its own workforces are taken into account in the decision-making processes of the undertaking.
""",
'S1-2_27': """
   - **Point 27:** The undertaking shall disclose whether and how the perspectives of its own workforce inform its decisions or activities aimed at managing the actual and potential impacts on its own workforce. This shall include, where relevant, an explanation of:
     - (a) whether engagement occurs directly with the undertaking’s own workforce or workers' representatives;
     - (b) the stage(s) at which engagement occurs, the type of engagement and frequency of the engagement;
     - (c) the function and the most senior role within the undertaking that has operational responsibility for ensuring that this engagement happens and that the results inform the undertaking’s approach;
     - (d) where applicable, a Global Framework Agreement or other agreements that the undertaking has with workers' representatives related to the respect of human rights of its own workforce , including an explanation of how the agreement enables the undertaking to gain insight into the perspectives of its own workforce; and
     - (e) where applicable, how the undertaking assesses the effectiveness of its engagement with its own workforce, including, where relevant, any agreements or outcomes that result.
""",
'S1-2_28': """
   - **Point 28:** Where applicable, the undertaking shall disclose the steps it takes to gain insight into the perspectives of people in its own workforce who may be particularly vulnerable to impacts and/or marginalised (for example, women, migrants, people with disabilities).
""",
'S1-2_29': """
   - **Point 29:** If the undertaking cannot disclose the above required information because it has not adopted a general process to engage with its own workforce , it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a process in place.
""",
'S1-3_30': """
   - **Point 30:** The undertaking shall describe the processes it has in place to provide for or cooperate in the remediation of negative impacts on people in its own workforce that the undertaking is connected with, as well as channels available to its own workforce to raise concerns and have them addressed.
""",
'S1-3_31': """
   - **Point 31:** The objective of this Disclosure Requirement is to enable an understanding of the formal means by which the undertaking’s own workforce can make their concerns and needs known directly to the undertaking and/or through which the undertaking supports the availability of such channels (for example, grievance mechanisms ) in the workplace, and how follow up is carried out with the people concerned regarding the issues raised and the effectiveness of these channels.
""",
'S1-3_32': """
   - **Point 32:** The undertaking shall describe the processes in place to cover the matters defined within paragraph 2 of the Objective section by disclosing the following information:
     - (a) its general approach to and processes for providing or contributing to remedy where it has caused or contributed to a material negative impact on people in its own workforce , including whether and how the undertaking assesses that the remedy provided is effective;
     - (b) any specific channels it has in place for its own workforce to raise their concerns or needs directly with the undertaking and have them addressed, including whether these are established by the undertaking itself and/or through participation in third-party mechanisms;
     - (c) whether or not the undertaking has a grievance /complaints handling mechanism related to employee matters and
     - (d) the processes through which the undertaking supports the availability of such channels in the workplace of its own workforce; and
     - (e) how it tracks and monitors issues raised and addressed, and, how it ensures the effectiveness of the channels, including through the involvement of stakeholders who are intended users.
""",
'S1-3_33': """
   - **Point 33:** The undertaking shall disclose whether and how it assesses that people in its own workforce are aware of, and trust, these structures or processes as a way to raise their concerns or needs and have them addressed. In addition, the undertaking shall disclose whether it has policies in place regarding the protection of individuals that use them, including workers’ representatives, against retaliation. If such information has been disclosed in accordance with ESRS G1-1, the undertaking may refer to that information.
""",
'S1-3_34': """
   - **Point 34:** If the undertaking cannot disclose the above required information because it has not adopted a channel for raising concerns and/or does not support the availability of such a channel in the workplace for its own workforce, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a channel in place.
""",
'S1-4_35': """
   - **Point 35:** The undertaking shall disclose how it takes action to address material negative and positive impacts, and to manage material risks and pursue material opportunities related to its own workforce, and the effectiveness of those actions.
""",
'S1-4_36': """
   - **Point 36:** The objective of this Disclosure Requirement is twofold. Firstly, it is to enable an understanding of any actions and initiatives through which the undertaking seeks to:
     - (a) to prevent, mitigate and remediate negative material impacts on its own workforce ; and/or
     - (b) to achieve positive material impacts for its own workforce.
""",
'S1-4_37': """
   Secondly, it is to enable an understanding of the ways in which the undertaking is addressing the material risks and pursuing the material opportunities related to its own workforce.
   - **Point 37:** The undertaking shall provide a summarised description of the action plans and resources to manage its material impacts, risks , and opportunities related to its own workforce in accordance with ESRS 2 MDR-A Actions and resources in relation to material sustainability matters .
""",
'S1-4_38': """
   - **Point 38:** In relation to the material impacts related to its own workforce , the undertaking shall describe:
     - (a) actions taken, planned or underway to prevent or mitigate material negative impacts on its own workforce;
     - (b) whether and how it has taken action to provide or enable remedy in relation to an actual material impact;
     - (c) any additional actions or initiatives it has in place with the primary purpose of delivering positive impacts for its own workforce; and
     - (d) how it tracks and assesses the effectiveness of these actions and initiatives in delivering outcomes for its own workforce.
""",
'S1-4_39': """
   - **Point 39:** In relation to paragraph 36, the undertaking shall describe the processes through which it identifies what action is needed and appropriate in response to a particular actual or potential negative impact on its own workforce .
""",
'S1-4_40': """
   - **Point 40:** In relation to material risks and opportunities , the undertaking shall describe:
     - (a) what action is planned or underway to mitigate material risks for the undertaking arising from its impacts and dependencies on its own workforce and how it tracks effectiveness in practice; and
     - (b) what action is planned or underway to pursue material opportunities for the undertaking in relation to its own workforce.
""",
'S1-4_41': """
   - **Point 41:** The undertaking shall disclose whether and how it ensures that its own practices do not cause or contribute to material negative impacts on own workforce , including, where relevant, its practices in relation to procurement, sales and data use. This may include disclosing what approach is taken when tensions arise between the prevention or mitigation of material negative impacts and other business pressures.
""",
'S1-4_42': """
   - **Point 42:** When disclosing the information required under paragraph 40, the undertaking shall consider ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets if it evaluates the effectiveness of an action by setting a target.
""",
'S1-4_43': """
   - **Point 43:** The undertaking shall disclose what resources are allocated to the management of its material impacts, with information that allows users to gain an understanding of how the material impacts are managed.
""",
'S1-5_44': """
   - **Point 44:** The undertaking shall disclose the time-bound and outcome-oriented targets it may have set related to:
     - (a) reducing negative impacts on its own workforce; and/or
     - (b) advancing positive impacts on its own workforce; and/or
     - (c) managing material risks and opportunities related to its own workforce.
""",
'S1-5_45': """
   - **Point 45:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking is using outcome-oriented targets to drive and measure its progress in addressing its material negative impacts and/or advancing positive impacts on its own workforce , and/or in managing material risks and opportunities related to its own workforce.
""",
'S1-5_46': """
   - **Point 46:** The summarised description of the targets set to manage its material impacts, risks and opportunities related to the undertaking’s own workforce shall contain the information requirements defined in ESRS 2 MDR-T.
""",
'S1-5_47': """
   - **Point 47:** The undertaking shall disclose the process for setting the targets , including whether and how the undertaking engaged directly with its own workforce or workers’ representatives in:
     - (a) setting any such targets;
     - (b) tracking the undertaking’s performance against them; and
     - (c) identifying any lessons or improvements as a result of the undertaking’s performance.
""",
'S1-6_48': """
   - **Point 48:** The undertaking shall describe key characteristics of employees in its own workforce.
""",
'S1-6_49': """
   - **Point 49:** The objective of this Disclosure Requirement is to provide insight into the undertaking’s approach to employment, including the scope and nature of impacts arising from its employment practices, to provide contextual information that aids an understanding of the information reported in other disclosures, and to serve as the basis for calculation for quantitative metrics to be disclosed under other disclosure requirements in this Standard.
""",
'S1-6_50': """
   - **Point 50:** In addition to the information required by paragraph 40(a)iii of ESRS 2 General Disclosures , the undertaking shall disclose:
     - (a) the total number of employees by head count, and breakdowns by gender and by country for countries in which the undertaking has 50 or more employees representing at least 10% of its total number of employees;
     - (b) the total number by head count or full time equivalent (FTE) of:
            i.  permanent employees, and breakdown by gender; 
            ii. temporary employees, and breakdown by gender; and
            iii. non-guaranteed hours employees, and breakdown by gender. 
     - (c) the total number of employees who have left the undertaking during the reporting period and the rate of employee turnover in the reporting period.
     - (d) a description of the methodologies and assumptions used to compile the data, including whether the numbers are reported:
            i.  in head count or full-time equivalent (FTE) (including an explanation of how FTE is defined); and 
            ii. at the end of the reporting period, as an average across the reporting period, or using another methodology.
     - (e) where applicable, a provision of contextual information necessary to understand the data (for example, to understand fluctuations in number of employees during the reporting period); and
     - (f) a cross-reference of the information reported under (a) above to the most representative number in the financial statements.
""",
'S1-6_51': """
   - **Point 51:** For the information specified in point (b) of paragraph 50, the undertaking may in addition disclose the breakdown by region.
""",
'S1-6_52': """
   - **Point 52:** The undertaking may disclose by head count or full time equivalent (FTE) the following information:
     - (a) full-time employees , and breakdowns by gender and by region; and
     - (b) part-time employees, and breakdowns by gender and by region.
""",
'S1-7_53': """
   - **Point 53:** The undertaking shall describe key characteristics of non-employees in its own workforce.
""",
'S1-7_54': """
   - **Point 54:** The objective of this Disclosure Requirement is to provide insight into the undertaking’s approach to employment, including the scope and nature of impacts arising from its employment practices, to provide contextual information that aids the understanding of the information reported in other disclosures, and to serve as the basis for calculation for quantitative metrics to be disclosed under other disclosure requirements in this Standard. It also allows an understanding of how much the undertaking relies on non-employees as part of its workforce.
""",
'S1-7_55': """
   - **Point 55:** The disclosure required by paragraph 53 shall include:
     - (a) a disclosure of the total number of non-employees in the undertaking’s own workforce , i.e., either people with contracts with the undertaking to supply labour (“self-employed people”) or people provided by undertakings primarily engaged in “employment activities” (NACE Code N78).
     - (b) an explanation of the methodologies and assumptions used to compile the data, including whether the number of non-employees is reported:
            i.  in headcount or full-time equivalent (FTE) (including a definition of how FTE is defined); and 
            ii. at the end of the reporting period, as an average across the reporting period, or using another methodology.
     - (c) where applicable, a provision of contextual information necessary to understand the data (for example, significant fluctuations in the number of non-employees in the undertaking’s own workforce during the reporting period and between the current and the previous reporting period).
""",
'S1-7_56': """
   - **Point 56:** For the information specified in point (a) of paragraph 55, the undertaking may disclose the most common types of non-employees (for example, self-employed people, people provided by undertakings primarily engaged in employment activities, and other types relevant to the undertaking), their relationship with the undertaking, and the type of work that they perform.
""",
'S1-7_57': """
   - **Point 57:** Where data is not available, the undertaking shall estimate the number and state that it has done so. When the undertaking performs estimates, it shall describe the basis of preparation of this estimation.
""",
'S1-8_58': """
   - **Point 58:** The undertaking shall disclose information on the extent to which the working conditions and terms of employment of its employees are determined or influenced by collective bargaining agreements and on the extent to which its employees are represented in social dialogue in the European Economic Area (EEA).
""",
'S1-8_59': """
   - **Point 59:** The objective of this Disclosure Requirement is to enable an understanding of the coverage of collective bargaining agreements and social dialogue for the undertaking’s own employees .
""",
'S1-8_60': """
   - **Point 60:** The undertaking shall disclose:
     - (a) the percentage of its total employees covered by collective bargaining agreements;
     - (b) in the EEA, whether it has one or more collective bargaining agreements and, if so, the overall percentage of its employees covered by such agreement(s) for each country in which it has significant employment, defined as at least 50 employees by head count representing at least 10% of its total number of employees; and
     - (c) outside the EEA, the percentage of its own employees covered by collective bargaining agreements by region.
""",
'S1-8_61': """
   - **Point 61:** For employees not covered by collective bargaining agreements, the undertaking may disclose whether it determines their working conditions and terms of employment based on collective bargaining agreements that cover its other employees or based on collective bargaining agreements from other undertakings.
""",
'S1-8_62': """
   - **Point 62:** The undertaking may disclose the extent to which the working conditions and terms of employment of non-employees in its own workforce are determined or influenced by collective bargaining agreements, including an estimate of the coverage rate.
""",
'S1-8_63': """
   - **Point 63:** The undertaking shall disclose the following information in relation to social dialogue :
     - (a) the global percentage of employees covered by workers’ representatives, reported at the country level for each EEA country in which the undertaking has significant employment; and
     - (b) the existence of any agreement with its employees for representation by a European Works Council (EWC), a Societas Europaea (SE) Works Council, or a Societas Cooperativa Europaea (SCE) Works Council.
""",
'S1-9_64': """
   - **Point 64:** The undertaking shall disclose the gender distribution at top management and the age distribution amongst its employees.
""",
'S1-9_65': """
   - **Point 65:** The objective of this Disclosure Requirement is to enable an understanding of gender diversity at top management level and the age distribution of its employees .
""",
'S1-9_66': """
   - **Point 66:** The undertaking shall disclose:
     - (a) the gender distribution in number and percentage at top management level; and
     - (b) the distribution of employees by age group: under 30 years old; 30-50 years old; over 50 years old.
""",
'S1-10_67': """
   - **Point 67:** The undertaking shall disclose whether or not its employees are paid an adequate wage, and if they are not all paid an adequate wage, the countries and percentage of employees concerned.
""",
'S1-10_68': """
   - **Point 68:** The objective of this Disclosure Requirement is to enable an understanding of whether or not all the undertaking’s employees are paid an adequate wage , in line with applicable benchmarks.
""",
'S1-10_69': """
   - **Point 69:** The undertaking shall disclose whether all its employees are paid an adequate wage , in line with applicable benchmarks. If so, stating this will be sufficient to fulfil this disclosure requirement and no further information is needed.
""",
'S1-10_70': """
   - **Point 70:** If not all its employees are paid an adequate wage in line with applicable benchmarks, the undertaking shall disclose the countries where employees earn below the applicable adequate wage benchmark and the percentage of employees that earn below the applicable adequate wage benchmark for each of these countries.
""",
'S1-10_71': """
   - **Point 71:** The undertaking may also disclose the information specified in this disclosure requirement with regard to non-employees in its workforce.
""",
'S1-11_72': """
   - **Point 72:** The undertaking shall disclose whether its employees are covered by social protection against loss of income due to major life events, and, if not, the countries where this is not the case.
""",
'S1-11_73': """
   - **Point 73:** The objective of this Disclosure Requirement is to enable an understanding of whether the undertaking’s employees are covered by social protection against loss of income due to major life events, and, if not, the countries where this is not the case.
""",
'S1-11_74': """
   - **Point 74:** The undertaking shall disclose whether all its employees are covered by social protection , through public programs or through benefits offered by the undertaking, against loss of income due to any of the following major life events:
     - (a) sickness;
     - (b) unemployment starting from when the own worker is working for the undertaking;
     - (c) employment injury and acquired disability;
     - (d) parental leave; and
     - (e) retirement.
""",
'S1-11_75': """
   If so, stating this is sufficient to fulfil this disclosure requirement and no further information is needed.
   - **Point 75:** If not all of its employees are covered by social protection in accordance with paragraph 72, the undertaking shall in addition disclose the countries where employees do not have social protection with regard to one or more of the types of events listed in paragraph 72 and for each of those countries the types of employees who do not have social protection with regard to each applicable major life event.
""",
'S1-11_76': """
   - **Point 76:** The undertaking may also disclose the information specified in this disclosure requirement with regard to non-employees in its workforce.
""",
'S1-12_77': """
   - **Point 77:** The undertaking shall disclose the percentage of its own employees with disabilities.
""",
'S1-12_78': """
   - **Point 78:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which persons with disabilities are included among the undertaking’s employees .
""",
'S1-12_79': """
   - **Point 79:** The undertaking shall disclose the percentage of persons with disabilities amongst its employees , subject to legal restrictions on the collection of data.
""",
'S1-12_80': """
   - **Point 80:** The undertaking may disclose the percentage of employees with disabilities with a breakdown by gender.
""",
'S1-13_81': """
   - **Point 81:** The undertaking shall disclose the extent to which training and skills development is provided to its employees.
""",
'S1-13_82': """
   - **Point 82:** The objective of this Disclosure Requirement is to enable an understanding of the training and skills development -related activities that have been offered to employees , within the context of continuous professional growth, to upgrade employees’ skills and facilitate continued employability.
""",
'S1-13_83': """
   - **Point 83:** The disclosure required by paragraph 81 shall include:
     - (a) the percentage of employees that participated in regular performance and career development reviews; such information shall be broken down by gender;
     - (b) the average number of training hours per employee and by gender.
""",
'S1-13_84': """
   - **Point 84:** The undertaking may disclose breakdowns by employee category for the percentage of employees that participated in regular performance and career development and for the average number of training hours per employee.
""",
'S1-13_85': """
   - **Point 85:** The undertaking may also disclose the information specified in this disclosure requirement with regard to non-employees in its workforce.
""",
'S1-14_86': """
   - **Point 86:** The undertaking shall disclose information on the extent to which its own workforce is covered by its health and safety management system and the number of incidents associated with work-related injuries, ill health and fatalities of its own workforce. In addition, it shall disclose the number of fatalities as a result of work-related injuries and work-related ill health of other workers working on the undertaking’s sites.
""",
'S1-14_87': """
   - **Point 87:** The objective of this Disclosure Requirement is to allow an understanding of the coverage, quality and performance of the health and safety management system established to prevent work-related injuries .
""",
'S1-14_88': """
   - **Point 88:** The disclosure required by paragraph 86 shall include the following information, where applicable broken down between employees and non-employees in the undertaking’s own workforce :
     - (a) the percentage of people in its own workforce who are covered by the undertaking’s health and safety management system based on legal requirements and/or recognised standards or guidelines;
     - (b) the number of fatalities ( 102 ) as a result of work-related injuries and work-related ill health ;
     - (c) the number and rate of recordable work-related accidents;
     - (d) with regard to the undertaking’s employees, the number of cases of recordable work-related ill health , subject to legal restrictions on the collection of data; and
     - (e) with regard to the undertaking’s employees, the number of days lost to work-related injuries and fatalities from work-related accidents, work-related ill health and fatalities from ill health.
""",
'S1-14_89': """
   The information for (b) shall also be reported for other workers working on the undertaking’s sites , such as value chain workers if they are working on the undertaking’s sites.
   - **Point 89:** The undertaking may also disclose the information specified in points (d) and (e) of paragraph 88 with regard to non-employees .
""",
'S1-14_90': """
   - **Point 90:** In addition, the undertaking may include the following additional information on the health and safety coverage: the percentage of its own workers covered by a health and safety management system which is based on legal requirements and/or recognised standards or guidelines and which has been internally audited and/or audited or certified by an external party.
""",
'S1-15_91': """
   - **Point 91:** The undertaking shall disclose the extent to which employees are entitled to and make use of family-related leave.
""",
'S1-15_92': """
   - **Point 92:** The objective of this Disclosure Requirement is to provide an understanding of the entitlement and actual practices amongst the employees to take family-related leave in a gender equitable manner, as it is one of the dimensions of work-life balance .
""",
'S1-15_93': """
   - **Point 93:** The disclosure required by paragraph 91 shall include:
     - (a) the percentage of employees entitled to take family-related leave; and
     - (b) the percentage of entitled employees that took family-related leave, and a breakdown by gender.
""",
'S1-15_94': """
   - **Point 94:** If all of the undertaking’s employees are entitled to family-related leave through social policy and/or collective bargaining agreements, it is sufficient to disclose this in order to meet the requirement of paragraph 93a.
""",
'S1-16_95': """
   - **Point 95:** The undertaking shall disclose the percentage gap in pay between its female and male employees and the ratio between the remuneration of its highest paid individual and the median remuneration for its employees.
""",
'S1-16_96': """
   - **Point 96:** The objective of this Disclosure Requirement is twofold: to allow an understanding of the extent of any gap in the pay between women and men amongst the undertaking’s employees ; and to provide insight into the level of remuneration inequality inside the undertaking and whether wide pay disparities exist.
""",
'S1-16_97': """
   - **Point 97:** The disclosure required by paragraph 95 shall include:
     - (a) the gender pay gap, defined as the difference of average pay levels between female and male employees, expressed as percentage of the average pay level of male employees;
     - (b) 	the annual total remuneration ratio of the highest paid individual to the median annual total remuneration for all employees (excluding the highest-paid individual); and
     - (c) 	where applicable, any contextual information necessary to understand the data and how the data has been compiled and other changes to the underlying data that are to be considered.
""",
'S1-16_98': """
   - **Point 98:** The undertaking may disclose a breakdown of the gender pay gap as defined in paragraph 97(a) by employee category and/or by country/segment. The undertaking may also disclose the gender pay gap between employees by categories of employees broken down by ordinary basic salary and complementary or variable components.
""",
'S1-16_94': """
   - **Point 99:** In relation to paragraph 97 (b), the undertaking may report this figure adjusted for purchasing power differences between countries, in which case it shall report the methodology used for the calculation.
""",
'S1-17_100': """
   - **Point 100:** The undertaking shall disclose the number of work-related incidents and/or complaints and severe human rights impacts within its own workforce, and any related fines, sanctions or compensation for the reporting period.
""",
'S1-17_101': """
   - **Point 101:** The objective of this Disclosure Requirement is to allow an understanding of the extent to which work-related incidents and severe cases of human rights impacts are affecting its own workforce.
""",
'S1-17_102': """
   - **Point 102:** The disclosure required by paragraph 100 shall include, subject to the relevant privacy regulations, work-related incidents of discrimination on the grounds of gender, racial or ethnic origin, nationality, religion or belief, disability, age, sexual orientation, or other relevant forms of discrimination involving internal and/or external stakeholders across operations in the reporting period. This includes incidents of harassment as a specific form of discrimination.
""",
'S1-17_103': """
   - **Point 103:** The undertaking shall disclose:
     - (a) the total number of incidents of discrimination , including harassment , reported in the reporting period;
     - (b) the number of complaints filed through channels for people in the undertaking’s own workforce to raise concerns (including grievance mechanisms) and, where applicable, to the National Contact Points for OECD Multinational Enterprises related to the matters defined in paragraph 2 of this Standard, excluding those already reported in (a) above;
     - (c) the total amount of fines, penalties, and compensation for damages as a result of the incidents and complaints disclosed above, and a reconciliation of such monetary amounts disclosed with the most relevant amount presented in the financial statements; and
     - (d) where applicable, contextual information necessary to understand the data and how such data has been compiled.
""",
'S1-17_104': """
   - **Point 104:** The undertaking shall disclose the following information regarding identified cases of severe human rights incidents (e.g., forced labour , human trafficking or child labour ):
     - (a) the number of severe human rights incidents connected to the undertaking’s workforce in the reporting period, including an indication of how many of these are cases of non-respect of the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises. If no such incidents have occurred, the undertaking shall state this; and
     - (b) the total amount of fines, penalties and compensation for damages for the incidents described in (a) above, and a reconciliation of the monetary amounts disclosed in the most relevant amount in the financial statements.
""",
'S2-1_14': """
   - **Point 14:** The undertaking shall describe its policies adopted to manage its material impacts on value chain workers, as well as associated material risks and opportunities.
""",
'S2-1_15': """
   - **Point 15:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of material impacts on value chain workers specifically, as well as policies that cover material risks or opportunities related to value chain workers.
""",
'S2-1_16': """
   - **Point 16:** The disclosure required by paragraph 14 shall contain the information on the undertaking’s policies to manage its material impacts, risks and opportunities related to value chain workers in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters . In addition, the undertaking shall specify whether such policies cover specific groups of value chain workers or all value chain workers.
""",
'S2-1_17': """
   - **Point 17:** The undertaking shall describe its human rights policy commitments ( 112 ) that are relevant to value chain workers , including those processes and mechanisms to monitor compliance with the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises ( 113 ) . In its disclosure, it shall focus on those matters that are material in relation to, as well as the general approach to:
     - (a) respect for the human rights, including labour rights, of workers;
     - (b) engagement with value chain workers; and
     - (c) measures to provide and/or enable remedy for human rights impacts.
""",
'S2-1_18': """
   - **Point 18:** The undertaking shall state whether its policies in relation to value chain workers explicitly address trafficking in human beings, forced labour or compulsory labour and child labour. It shall also state whether the undertaking has a supplier code of conduct.
""",
'S2-1_19': """
   - **Point 19:** The undertaking shall disclose whether and how its policies with regard to value chain workers are aligned with internationally recognised instruments relevant to value chain workers, including the United Nations (UN) Guiding Principles on Business and Human Rights. The undertaking shall also disclose the extent to which cases of non-respect of the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises that involve value chain workers have been reported in its upstream and downstream value chain and, if applicable, an indication of the nature of such cases.
""",
'S2-2_20': """
   - **Point 20:** The undertaking shall disclose its general processes for engaging with value chain workers and their representatives about actual and potential impacts on them.
""",
'S2-2_21': """
   - **Point 21:** The objective of this Disclosure Requirement is to enable an understanding of whether and how the undertaking engages, as part of its ongoing due diligence process, with value chain workers and their legitimate representatives, or with credible proxies , about material actual and potential positive and/or negative impacts that do or are likely to affect them, and whether and how perspectives of value chain workers are taken into account in the decision-making processes of the undertaking.
""",
'S2-2_22': """
   - **Point 22:** The undertaking shall disclose whether and how the perspectives of value chain workers inform its decisions or activities aimed at managing the actual and potential impacts on value chain workers. This shall include, where relevant, an explanation of:
     - (a) whether engagement occurs with value chain workers or their legitimate representatives directly, or with credible proxies that have insight into their situation;
     - (b) the stage(s) at which engagement occurs, the type of engagement, and the frequency of the engagement;
     - (c) the function and the most senior role within the undertaking that has operational responsibility for ensuring that this engagement happens, and that the results inform the undertaking’s approach;
     - (d) where applicable, Global Framework Agreements or for agreements that the undertaking has with global union federations related to respect of human rights of workers in the value chain, including their right to bargain collectively, and including an explanation of how the agreement enables the undertaking to gain insight into those workers’ perspectives; and
     - (e) where applicable, how the undertaking assesses the effectiveness of its engagement with workers in the value chain, including, where relevant, any agreements or outcomes that result.
""",
'S2-2_23': """
   - **Point 23:** Where applicable, the undertaking shall disclose the steps it takes to gain insight into the perspectives of workers that may be particularly vulnerable to impacts and/or marginalised (for example, women workers, migrant workers, workers with disabilities).
""",
'S2-2_24': """
   - **Point 24:** If the undertaking cannot disclose the above required information because it has not adopted a general process to engage with workers in the value chain, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a process in place.
""",
'S2-3_25': """
   - **Point 25:** The undertaking shall describe the processes it has in place to provide for or cooperate in the remediation of negative impacts on value chain workers that the undertaking is connected with, as well as channels available to value chain workers to raise concerns and have them addressed.
""",
'S2-3_26': """
   - **Point 26:** The objective of this Disclosure Requirement is to enable an understanding of the formal means by which value chain workers can make their concerns and needs known directly to the undertaking and/or through which the undertaking supports the availability of such channels (for example, grievance mechanisms ) in the workplace of value chain workers, how follow up is carried out with these workers regarding the issues raised, and the effectiveness of these channels.
""",
'S2-3_27': """
   - **Point 27:** The undertaking shall describe:
     - (a) its general approach to and processes for providing or contributing to remedy where it has caused or contributed to a material negative impact on value chain workers , including whether and how the undertaking assesses that the remedy provided is effective;
     - (b) any specific channels it has in place for value chain workers to raise their concerns or needs directly with the undertaking and have them addressed, including whether these are established by the undertaking itself and/or whether they are third-party mechanisms;
     - (c) the processes through which it supports or requires the availability of such channels in the workplace of value chain workers; and
     - (d) how it tracks and monitors issues raised and addressed, and how it ensures the effectiveness of the channels, including through involvement of stakeholders who are the intended users .
""",
'S2-3_28': """
   - **Point 28:** The undertaking shall disclose whether and how it assesses that value chain workers are aware of and trust these structures or processes as a way to raise their concerns or needs and have them addressed. In addition, the undertaking shall disclose whether it has policies in place regarding the protection of individuals that use them against retaliation. If such information has been disclosed in accordance with ESRS G1-1, the undertaking may refer to that information.
""",
'S2-3_29': """
   - **Point 29:** If the undertaking cannot disclose the above required information because it has not adopted a channel for raising concerns and/or does not support the availability of such a channel in the workplace of value chain workers, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a channel or processes in place.
""",
'S2-4_30': """
   - **Point 30:** The undertaking shall disclose how it takes action to address material impacts on consumers and end-users, and to manage material risks and pursue material opportunities related to consumers and end-users, and effectiveness of those actions.
""",
'S2-4_31': """
   - **Point 31:** The objective of this Disclosure Requirement is twofold. Firstly, it is to provide an understanding of any actions and initiatives through which the undertaking seeks to:
     - (a) prevent, mitigate and remediate the negative material impacts on consumers and/or end-users , and/or
     - (b) achieve positive material impacts for consumers and/or end-users.
   Secondly, it is to enable an understanding of the ways in which the undertaking is addressing the material risks and pursuing the material opportunities related to consumers and/or end-users.
   The undertaking shall provide a summarised description of the action plans and resources to manage its material impacts, risks, and opportunities related to consumers and end-users as per ESRS 2 MDR-A Actions and resources in relation to material sustainability matters .
""",
'S2-4_32': """
   - **Point 32:** In relation to material impacts, the undertaking shall describe:
     - (a) actions taken, planned or underway to prevent, mitigate or remediate material negative impacts on consumers and/or end-users;
     - (b) whether and how it has taken action to provide or enable remedy in relation to an actual material impact;
     - (c) any additional actions or initiatives it has in place with the primary purpose of positively contributing to improved social outcomes for consumers and/or end-users; and
     - (d) how it tracks and assesses the effectiveness of these actions and initiatives in delivering intended outcomes for consumers and/or end-users.
""",
'S2-4_33': """
   - **Point 33:** In relation to paragraph 30, the undertaking shall describe:
     - (a) the processes through which it identifies what action is needed and appropriate in response to a particular actual or potential negative impact on value chain workers ;
     - (b) its approach to taking action in relation to specific material negative impacts on value chain workers, including any action in relation to its own purchasing or other internal practices, as well as capacity- building or other forms of engagement with entities in the value chain, or forms of collaborative action with industry peers or other relevant parties; and
     - (c) how it ensures that processes to provide or enable remedy in the event of material negative impacts are available and effective in their implementation and outcomes.
""",
'S2-4_34': """
   - **Point 34:** In relation to material risks and opportunities, the undertaking shall describe:
     - (a) what action is planned or underway to mitigate material risks for the undertaking arising from its impacts and dependencies on consumers and/or end-users and how it tracks effectiveness in practice; and
     - (b) what action is planned or underway to pursue material opportunities for the undertaking in relation to consumers and/or end-users.
""",
'S2-4_35': """
   - **Point 35:** The undertaking shall disclose whether and how it takes action to avoid causing or contributing to material negative impacts on consumers and/or end-users through its own practices, including, where relevant, in relation to marketing, sales and data use. This may include disclosing what approach is taken when tensions arise between the prevention or mitigation of material negative impacts and other business pressures.
""",
'S2-4_36': """
   - **Point 36:** The undertaking shall also disclose whether severe human rights issues and incidents connected to its upstream and downstream value chain have been reported and, if applicable, disclose these.
""",
'S2-4_37': """
   - **Point 37:** When disclosing the information required under paragraph 32 (c), the undertaking shall consider ESRS 2 (see ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets ) if it evaluates the effectiveness of an action by setting a target.
""",
'S2-4_30': """
   - **Point 38:** The undertaking shall disclose what resources are allocated to the management of its material impacts, with information that enables users to gain an understanding of how the material impacts are managed.
""",
'S2-5_39': """
   - **Point 39:** The undertaking shall disclose the time-bound and outcome-oriented targets it may have set related to:
     - (a) reducing negative impacts on consumers and/or end-users; and/or
     - (b) advancing positive impacts on consumers and/or end-users; and/or
     - (c) managing material risks and opportunities related to consumers and/or end-users.
""",
'S2-5_40': """
   - **Point 40:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking is using time-bound and outcome-oriented targets to drive and measure its progress in addressing material negative impacts, and/or advancing positive impacts on value chain workers, and/or in managing material risks and opportunities related to value chain workers.
""",
'S2-5_41': """
   - **Point 41:** The summarised description of the targets to manage its material impacts, risks and opportunities related to consumers and/or end-users shall contain the information requirements defined in ESRS 2 MDR-T.
""",
'S2-5_42': """
   - **Point 42:** The undertaking shall disclose the process for setting the targets , including whether and how the undertaking engaged directly with consumers and/or end-users , their legitimate representatives, or with credible proxies that have insight into their situation in:
     - (a) setting any such targets;
     - (b) tracking the undertaking’s performance against them; and
     - (c) identifying, if any, lessons or improvements as a result of the undertaking’s performance.
""",
'S3-1_12': """
   - **Point 12:** The undertaking shall describe its policies adopted to manage its material impacts on affected communities, as well as associated material risks and opportunities.
""",
'S3-1_13': """
   - **Point 13:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of material impacts on affected communities specifically, as well as policies that cover material risks or opportunities related to affected communities.
""",
'S3-1_14': """
   - **Point 14:** The disclosure required by paragraph 12 shall contain the information on the undertaking’s policies to manage its material impacts, risks and opportunities related to affected communities in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters . In addition, the undertaking shall specify if such policies cover specific affected communities or all affected communities.
""",
'S3-1_15': """
   - **Point 15:** The undertaking shall disclose any particular policy provisions for preventing and addressing impacts on indigenous peoples .
""",
'S3-1_16': """
   - **Point 16:** The undertaking shall describe its human rights policy commitments ( 119 ) that are relevant to affected communities, including those processes and mechanisms to monitor compliance with the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises. In its disclosure it shall focus on those matters that are material in relation to ( 120 ) , as well as its general approach to:
     - (a) respect for the human rights of communities, and indigenous peoples specifically;
     - (b) engagement with affected communities; and
     - (c) measures to provide and/or enable remedy for human rights impacts.
""",
'S3-1_17': """
   - **Point 17:** The undertaking shall disclose whether and how its policies with regard to affected communities are aligned with internationally recognised standards relevant to communities and indigenous peoples specifically, including the United Nations (UN) Guiding Principles on Business and Human Rights. The undertaking shall also disclose the extent to which cases of non-respect of the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises that involve affected communities have been reported in its own operations or in its upstream and downstream value chain and, if applicable, an indication of the nature of such cases.
""",
'S3-1_18': """
   - **Point 18:** The policy may take the form of a stand-alone policy regarding communities or be included in a broader document such as a code of ethics or a general sustainability policy that has already been disclosed by the undertaking as part of another ESRS. In those cases, the undertaking shall provide an accurate cross-reference to identify the aspects of the policy that satisfy the requirements of this Disclosure Requirement.
""",
'S3-2_19': """
   - **Point 19:** The undertaking shall disclose its general processes for engaging with affected communities and their representatives about actual and potential impacts on them.
""",
'S3-2_20': """
   - **Point 20:** The objective of this Disclosure Requirement is to enable an understanding of whether and how the undertaking engages, as part of its ongoing due diligence process, with affected communities, their legitimate representatives, or with credible proxies , about material actual and potential positive and/or negative impacts that do or are likely to affect them, and whether and how perspectives of affected communities are taken into account in the decision-making processes of the undertaking.
""",
'S3-2_21': """
   - **Point 21:** The undertaking shall disclose whether and how the perspectives of affected communities inform its decisions or activities aimed at managing actual and potential impacts on communities. This shall include, where relevant, an explanation of:
     - (a) whether engagement occurs with affected communities or their legitimate representatives directly, or with credible proxies that have insight into their situation;
     - (b) the stage(s) at which engagement occurs, the type of engagement, and the frequency of the engagement;
     - (c) the function and the most senior role within the undertaking that has operational responsibility for ensuring this engagement happens, and that the results inform the undertaking’s approach;
     - (d) where applicable, how the undertaking assesses the effectiveness of its engagement with affected communities, including, where relevant, any agreements or outcomes that result.
""",
'S3-2_22': """
   - **Point 22:** Where applicable, the undertaking shall disclose the steps it takes to gain insight into the perspectives of affected communities that may be particularly vulnerable to impacts and/or marginalised, and into the perspective of specific groups within the affected communities, such as women and girls.
""",
'S3-2_23': """
   - **Point 23:** Where affected communities are indigenous peoples , the undertaking shall also disclose how it takes into account and ensures respect of their particular rights in its stakeholder engagement approach, including their right to free, prior and informed consent with regard to: (i) their cultural, intellectual, religious and spiritual property; (ii) activities affecting their lands and territories; and (iii) legislative or administrative measures that affect them. In particular, where engagement occurs with indigenous peoples, the undertaking shall also disclose whether and how indigenous peoples have been consulted on the mode and parameters of the engagement (for example, in designing the agenda, nature, and timeliness of the engagement).
""",
'S3-2_24': """
   - **Point 24:** If the undertaking cannot disclose the above required information because it has not adopted a general process to engage with affected communities, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a process in place..
""",
'S3-3_25': """
   - **Point 25:** The undertaking shall describe the processes it has in place to provide for or cooperate in the remediation of negative impacts on affected communities that the undertaking is connected with, as well as channels available to affected communities to raise concerns and have them addressed.
""",
'S3-3_26': """
   - **Point 26:** The objective of this Disclosure Requirement is to enable an understanding of the formal means by which affected communities can make their concerns and needs known directly to the undertaking, and/or through which the undertaking supports the availability of such channels (for example, grievance mechanisms ) by its business relationships, how follow up is performed with these communities regarding the issues raised, and the effectiveness of these channels.
""",
'S3-3_27': """
   - **Point 27:** The undertaking shall describe:
     - (a) its general approach to and processes for providing or contributing to remedy where it has identified that it has caused or contributed to a material negative impact on affected communities, including whether and how the undertaking assesses that the remedy provided is effective;
     - (b) any specific channels it has in place for affected communities to raise their concerns or needs directly with the undertaking and have them addressed, including whether these are established by the undertaking itself and/or through participation in third-party mechanisms;
     - (c) its processes through which the undertaking supports the availability of such channels by its business relationships; and
     - (d) how it tracks and monitors issues raised and addressed, and how it ensures the effectiveness of the channels, including through involvement of stakeholders who are the intended users of those channels.
""",
'S3-3_28': """
   - **Point 28:** The undertaking shall disclose whether and how it assesses that affected communities are aware of and trust these structures or processes as a way to raise their concerns or needs and have them addressed. In addition, the undertaking shall disclose whether it has policies in place regarding the protection of individuals that use them against retaliation. If such information has been disclosed in accordance with ESRS G1-1, the undertaking may refer to that information.
""",
'S3-3_29': """
   - **Point 29:** If the undertaking cannot disclose the above required information because it has not adopted a channel for raising concerns and/or does not support the availability of such a channel by its business relationships, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a channel or processes in place.
""",
'S3-4_30': """
   - **Point 30:** The undertaking shall disclose how it takes action to address material impacts on affected communities, and to manage material risks and pursue material opportunities related to affected communities and the effectiveness of those actions.
""",
'S3-4_31': """
   - **Point 31:** The objective of this Disclosure Requirement is twofold. Firstly, it is to provide an understanding of any actions and initiatives through which the undertaking seeks to:
     - (a) prevent, mitigate and remediate the negative material impacts on affected communities; and/or
     - (b) achieve positive material impacts for affected communities.
   Secondly, it is to enable an understanding of the ways in which the undertaking is addressing the material risks and pursuing the material opportunities related to affected communities.
   The undertaking shall provide a summarised description of the action plans and resources to manage its material impacts, risks, and opportunities related to affected communities as per ESRS 2 MDR-A Actions and resources in relation to material sustainability matters.
""",
'S3-4_32': """
   - **Point 32:** In relation to material impacts, the undertaking shall describe:
     - (a) actions taken, planned or underway to prevent or mitigate material negative impacts on affected communities;
     - (b) whether and how it has taken action to provide or enable remedy in relation to an actual material impact;
     - (c) any additional actions or initiatives it has in place with the primary purpose of delivering positive impacts for affected communities; and
     - (d) how it tracks and assesses the effectiveness of these actions and intiatives in delivering intended outcomes for affected communities.
""",
'S3-4_33': """
   - **Point 33:** In relation to paragraph 30, the undertaking shall describe:
     - (a) the processes through which it identifies what action is needed and appropriate in response to a particular actual or potential negative impact on affected communities;
     - (b) its approach to taking action in relation to specific material negative impacts on communities, including any action in relation to its own practices regarding land acquisition, planning and construction, operation or closure practices, as well as whether wider industry or collaborative action with other relevant parties will be required; and
     - (c) how it ensures that processes to provide or enable remedy in the event of material negative impacts are available and effective in their implementation and outcomes.
""",
'S3-4_34': """
   - **Point 34:** In relation to material risks and opportunities, the undertaking shall describe:
     - (a) what action is planned or underway to mitigate material risks for the undertaking arising from its impacts and dependencies on affected communities and how it tracks effectiveness in practice; and
     - (b) what action is planned or underway to pursue material opportunities for the undertaking in relation to affected communities.
""",
'S3-4_35': """
   - **Point 35:** The undertaking shall disclose whether and how it takes action to avoid causing or contributing to material negative impacts on affected communities through its own practices, including, where relevant, in relation to planning, land acquisition and exploitation, finance, extraction or production of raw materials, use of natural resources, and management of environmental impacts. This may include disclosing what approach is taken when tensions arise between the prevention or mitigation of material negative impacts and other business pressures.
""",
'S3-4_36': """
   - **Point 36:** The undertaking shall also disclose whether severe human rights issues and incidents connected to affected communities have been reported and, if applicable, disclose these.
""",
'S3-4_37': """
   - **Point 37:** When disclosing the information required under paragraph 32 (d), the undertaking shall consider ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets if it evaluates the effectiveness of an action by setting a target.
""",
'S3-4_38': """
   - **Point 38:** The undertaking shall disclose what resources are allocated to the management of its material impacts, with information that enables users to gain an understanding of how the material impacts are managed.
""",
'S3-5_39': """
   - **Point 39:** The undertaking shall disclose the time-bound and outcome-oriented targets it may have set related to:
     - (a) reducing negative impacts on affected communities; and/or
     - (b) advancing positive impacts on affected communities; and/or
     - (c) managing material risks and opportunities related to affected communities.
""",
'S3-5_40': """
   - **Point 40:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking is using time-bound and outcome-oriented targets to drive and measure its progress in addressing material negative impacts, and/or advancing positive impacts on affected communities, and/or in managing material risks and opportunities related to affected communities.
""",
'S3-5_41': """
   - **Point 41:** The summarised description of the targets to manage its material impacts, risks and opportunities related to affected communities shall contain the information requirements defined in ESRS 2 MDR-T.
""",
'S3-5_42': """
   - **Point 42:** The undertaking shall disclose the process for setting the targets , including whether and how the undertaking engaged directly with affected communities, their legitimate representatives, or with credible proxies that have insight into their situation in:
     - (a) setting any such targets;
     - (b) atracking the undertaking’s performance against them; and
     - (c) identifying, any, lessons or improvements as a result of the undertaking’s performance.
""",
'S4-1_13': """
   - **Point 13:** The undertaking shall describe its policies adopted to manage its material impacts of its products and/or services on consumers and end-users, as well as associated material risks and opportunities.
""",
'S4-1_14': """
   - **Point 14:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of material impacts on consumers and/or end-users specifically, as well as policies that cover material risks or opportunities related to consumers and/or end-users.
""",
'S4-1_15': """
   - **Point 15:** The disclosure required by paragraph 13 shall contain the information on the undertaking’s policies to manage its material impacts, risks and opportunities related to consumers and/or end-users in accordance with ESRS 2 MDR-P Policies adopted to manage material sustainability matters . In addition, the undertaking shall specify if such policies cover specific groups or all consumers and/or end-users.
""",
'S4-1_16': """
   - **Point 16:** The undertaking shall describe its human rights policy commitments ( 123 ) that are relevant to consumers and/or end-users, including those processes and mechanisms to monitor compliance with the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises. In its disclosure it shall focus on those matters that are material, as well as the general approach in relation to:
     - (a) respect for the human rights of consumers and/or end-users;
     - (b) engagement with consumers and/or end-users; and
     - (c) measures to provide and/or enable remedy for human rights impacts.
""",
'S4-1_17': """
   - **Point 17:** The undertaking shall disclose whether and how its policies with regard to consumers and/or end-users are aligned with internationally recognised instruments relevant to consumers and/or end-users, including United Nations (UN) Guiding Principles on Business and Human Rights. The undertaking shall also disclose the extent to which cases of non-respect of the UN Guiding Principles on Business and Human Rights, ILO Declaration on Fundamental Principles and Rights at Work or OECD Guidelines for Multinational Enterprises that involve consumers and/or end-users have been reported in its downstream value chain and, if applicable, an indication of the nature of such cases.
""",
'S4-2_18': """
   - **Point 18:** The undertaking shall disclose its general processes for engaging with consumers and end-users and their representatives about actual and potential impacts on them.
""",
'S4-2_19': """
   - **Point 19:** The objective of this Disclosure Requirement is to enable an understanding of whether and how the undertaking engages, as part of its ongoing due diligence process, with consumers and/or end-users , their legitimate representatives, or with credible proxies , about material actual and potential positive and/or negative impacts that do or are likely to affect them, and whether and how perspectives of consumers and/or end-users are taken into account in the decision-making processes of the undertaking.
""",
'S4-2_20': """
   - **Point 20:** The undertaking shall disclose whether and how the perspectives of consumers and/or end-users inform its decisions or activities aimed at managing actual and potential impacts on consumers and/or end-users. This shall include, where relevant, an explanation of:
     - (a) whether engagement occurs with affected consumers and/or end-users or their legitimate representatives directly, or with credible proxies that have insight into their situation;
     - (b) the stage(s) at which engagement occurs, the type of engagement, and the frequency of the engagement;
     - (c) the function and the most senior role within the undertaking that has operational responsibility for ensuring this engagement happens and that the results inform the undertaking’s approach; and
     - (d) where applicable, how the undertaking assesses the effectiveness of its engagement with consumers and/or end-users, and, where relevant, any agreements or outcomes that result from such engagement.
""",
'S4-2_21': """
   - **Point 21:** Where applicable, the undertaking shall disclose the steps it takes to gain insight into the perspectives of consumers and/or end-users that may be particularly vulnerable to impacts and/or marginalised (for example, people with disabilities, children, etc.).
""",
'S4-2_22': """
   - **Point 22:** If the undertaking cannot disclose the above required information because it has not adopted a general process to engage with consumers and/or end-users , it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a process in place.
""",
'S4-3_23': """
   - **Point 23:** The undertaking shall describe the processes it has in place to provide for or cooperate in the remediation of negative impacts on consumers and end-users that the undertaking is connected with, as well as channels available to consumers and end-users to raise concerns and have them addressed.
""",
'S4-3_24': """
   - **Point 24:** The objective of this Disclosure Requirement is to enable an understanding of the formal means by which consumers and/or end-users can make their concerns and needs known directly to the undertaking, and/or through which the undertaking supports the availability of such channels (for example, grievance mechanisms ) by its business relationships, how follow up is performed with these consumers and/or end-users regarding the issues raised, and the effectiveness of these channels.
""",
'S4-3_25': """
   - **Point 25:** The undertaking shall describe:
     - (a) its general approach to and processes for providing or contributing to remedy where it has identified that it has caused or contributed to a material negative impact on consumers and/or end-users, including whether and how the undertaking assesses that the remedy provided is effective;
     - (b) any specific channels it has in place for consumers and/or end-users to raise their concerns or needs directly with the undertaking and have them addressed, including whether these are established by the undertaking itself and/or through participation in third-party mechanisms;
     - (c) the processes through which the undertaking supports or requires the availability of such channels by its business relationships; and
     - (d) how it tracks and monitors issues raised and addressed, and how it ensures the effectiveness of the channels, including through involvement of stakeholders who are the intended users.
""",
'S4-3_26': """
   - **Point 26:** The undertaking shall disclose whether and how it assesses that consumers and/or end-users are aware of and trust these structures or processes as a way to raise their concerns or needs and have them addressed. In addition, the undertaking shall disclose whether it has policies in place to protect individuals from retaliation when they use such structures or processes. If such information has been disclosed in accordance with ESRS G1-1, the undertaking may refer to that information.
""",
'S4-3_27': """
   - **Point 27:** If the undertaking cannot disclose the above required information because it has not adopted a channel for raising concerns and/or does not support the availability of mechanisms by its business relationships, it shall disclose this to be the case. It may disclose a timeframe in which it aims to have such a channel or processes in place.
""",
'S4-4_28': """
   - **Point 28:** The undertaking shall disclose how it takes action to address material impacts on consumers and end-users, and to manage material risks and pursue material opportunities related to consumers and end-users, and effectiveness of those actions.
""",
'S4-4_29': """
   - **Point 29:** The objective of this Disclosure Requirement is twofold. Firstly, it is to provide an understanding of any actions and initiatives through which the undertaking seeks to:
     - (a) prevent, mitigate and remediate the negative material impacts on consumers and/or end-users , and/or
     - (b) achieve positive material impacts for consumers and/or end-users.
   Secondly, it is to enable an understanding of the ways in which the undertaking is addressing the material risks and pursuing the material opportunities related to consumers and/or end-users.
""",
'S4-4_30': """
   - **Point 30:** The undertaking shall provide a summarised description of the action plans and resources to manage its material impacts, risks, and opportunities related to consumers and end-users as per ESRS 2 MDR-A Actions and resources in relation to material sustainability matters .
""",
'S4-4_31': """
   - **Point 31:** In relation to material impacts, the undertaking shall describe:
     - (a) actions taken, planned or underway to prevent, mitigate or remediate material negative impacts on consumers and/or end-users;
     - (b) whether and how it has taken action to provide or enable remedy in relation to an actual material impact;
     - (c) any additional actions or initiatives it has in place with the primary purpose of positively contributing to improved social outcomes for consumers and/or end-users; and
     - (d) how it tracks and assesses the effectiveness of these actions and initiatives in delivering intended outcomes for consumers and/or end-users.
""",
'S4-4_32': """
   - **Point 32:** In relation to paragraph 28, the undertaking shall describe:
     - (a) the processes through which it identifies what action is needed and appropriate in response to a particular actual or potential negative impact on consumers and/or end-users;
     - (b) its approaches to taking action in relation to specific material negative impacts on consumers and/or end-users, including any action in relation to its own practices regarding product design, marketing or sales, as well as whether wider industry or collaborative action with other relevant parties will be required; and
     - (c) how it ensures that processes to provide or enable remedy in the event of material negative impacts are available and effective in their implementation and outcomes.
""",
'S4-4_33': """
   - **Point 33:** In relation to material risks and opportunities, the undertaking shall describe:
     - (a) what action is planned or underway to mitigate material risks for the undertaking arising from its impacts and dependencies on consumers and/or end-users and how it tracks effectiveness in practice; and
     - (b) what action is planned or underway to pursue material opportunities for the undertaking in relation to consumers and/or end-users.
""",
'S4-4_34': """
   - **Point 34:** The undertaking shall disclose whether and how it takes action to avoid causing or contributing to material negative impacts on consumers and/or end-users through its own practices, including, where relevant, in relation to marketing, sales and data use. This may include disclosing what approach is taken when tensions arise between the prevention or mitigation of material negative impacts and other business pressures.
""",
'S4-4_35': """
   - **Point 35:** When preparing this disclosure, the undertaking shall consider whether severe human rights issues and incidents connected to its consumers and/or end-users have been reported and, if applicable, disclose these.
""",
'S4-4_36': """
   - **Point 36:** Where the undertaking evaluates the effectiveness of an action by setting a target, in disclosing the information required under paragraph 31(d), the undertaking shall consider ESRS 2 MDR-T Tracking effectiveness of policies and actions through targets .
""",
'S4-4_37': """
   - **Point 37:** The undertaking shall disclose what resources are allocated to the management of its material impacts with information that enables users to gain an understanding of how the material impacts are managed.
""",
'S4-5_38': """
   - **Point 38:** The undertaking shall disclose the time-bound and outcome-oriented targets it may have set related to:
     - (a) reducing negative impacts on consumers and/or end-users; and/or
     - (b) advancing positive impacts on consumers and/or end-users; and/or
     - (c) managing material risks and opportunities related to consumers and/or end-users.
""",
'S4-5_39': """
   - **Point 39:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking is using time-bound and outcome-oriented targets to drive and measure progress in addressing material negative impacts, and/or advancing positive impacts on consumers and/or end-users , and/or in managing material risks and opportunities related to consumers and/or end-users.
""",
'S4-5_40': """
   - **Point 40:** The summarised description of the targets to manage its material impacts, risks and opportunities related to consumers and/or end-users shall contain the information requirements defined in ESRS 2 MDR-T.
""",
'S4-5_41': """
   - **Point 41:** The undertaking shall disclose the process for setting the targets , including whether and how the undertaking engaged directly with consumers and/or end-users , their legitimate representatives, or with credible proxies that have insight into their situation in:
     - (a) setting any such targets;
     - (b) tracking the undertaking’s performance against them; and
     - (c) identifying, if any, lessons or improvements as a result of the undertaking’s performance.
""",
'G1-1_7': """
   - **Point 7:** The undertaking shall disclose its policies with respect to business conduct matters and how it fosters its corporate culture.
""",
'G1-1_8': """
   - **Point 8:** The objective of this Disclosure Requirement is to enable an understanding of the extent to which the undertaking has policies that address the identification, assessment, management and/or remediation of its material impacts, risks and opportunities related to business conduct matters. It also aims to provide an understanding of the undertaking’s approach to corporate culture .
""",
'G1-1_9': """
   - **Point 9:** The disclosures required under paragraph 7 shall include how the undertaking establishes, develops, promotes and evaluates its corporate culture.
""",
'G1-1_10': """
   - **Point 10:** The disclosures in paragraph 7 shall cover the following aspects related to the undertaking’s policies on business conduct matters:
     - (a) a description of the mechanisms for identifying, reporting and investigating concerns about unlawful behaviour or behaviour in contradiction of its code of conduct or similar internal rules; and whether it accommodates reporting from internal and/or external stakeholders ;
     - (b) where the undertaking has no policies on anti- corruption or anti- bribery consistent with the United Nations Convention against Corruption ( 127 ) , it shall state this and whether it has plans to implement them and the timetable for implementation;
     - (c) how the undertaking protects whistleblowers, including:
        i.  details on the establishment of internal whistleblower reporting channels, including whether the undertaking provides for information and training to its own workers and information about the designation and training of staff receiving reports; and
        ii. measures to protect against retaliation its own workers who are whistleblowers in accordance with the applicable law transposing Directive (EU) 2019/1937 of the European Parliament and of the Council ( 128 ) ;
     - (d) where the undertaking has no policies on the protection of whistle-blowers ( 129 ) , it shall state this and whether it has plans to implement them and the timetable for implementation;
     - (e) beyond the procedures to follow-up on reports by whistleblowers in accordance with the applicable law transposing Directive (EU) 2019/1937, whether the undertaking has procedures to investigate business conduct incidents , including incidents of corruption and bribery , promptly, independently and objectively;
     - (f) where applicable, whether the undertaking has in place policies with respect to animal welfare;
     - (g) the undertaking’s policy for training within the organisation on business conduct, including target audience, frequency and depth of coverage; and
     - (h)the functions within the undertaking that are most at risk in respect of corruption and bribery .
""",
'G1-1_11': """
   - **Point 11:** Undertakings that are subject to legal requirements under national law transposing Directive (EU) 2019/1937, or to equivalent legal requirements with regard to the protection of whistle-blowers, may comply with the disclosure specified in paragraph 10 (d) by stating that they are subject to those legal requirements.
""",
'G1-2_12': """
   - **Point 12:** The undertaking shall provide information about the management of its relationships with its suppliers and its impacts on its supply chain.
""",
'G1-2_13': """
   - **Point 13:** The objective of this Disclosure Requirement is to provide an understanding of the undertaking’s management of its procurement process including fair behaviour with suppliers .
""",
'G1-2_14': """
   - **Point 14:** The undertaking shall provide a description of its policy to prevent late payments, specifically to SMEs.
""",
'G1-2_15': """
   - **Point 15:** The disclosure required under paragraph 12 shall include the following information:
     - (a) the undertaking’s approach to its relationships with its suppliers , taking account of risks to the undertaking related to its supply chain and of impacts on sustainability matters ; and
     - (b) whether and how it takes into account social and environmental criteria for the selection of its suppliers.
""",
'G1-3_16': """
   - **Point 16:** The undertaking shall provide information about its system to prevent and detect, investigate, and respond to allegations or incidents relating to corruption and bribery including the related training.
""",
'G1-3_17': """
   - **Point 17:** The objective of this Disclosure Requirement is to provide transparency on the key procedures of the undertaking to prevent, detect, and address allegations about corruption and bribery . This includes the training provided to own workers and/or information provided internally or to suppliers .
""",
'G1-3_18': """
   - **Point 18:** The disclosure required under paragraph 16 shall include the following information:
     - (a) a description of the procedures in place to prevent, detect, and address allegations or incidents of corruption and bribery ;
     - (b) whether the investigators or investigating committee are separate from the chain of management involved in the matter; and
     - (c) the process, if any, to report outcomes to the administrative, management and supervisory bodies .
""",
'G1-3_19': """
   - **Point 19:** Where the undertaking has no such procedures in place, it shall disclose this fact and, where applicable, its plans to adopt them.
""",
'G1-3_20': """
   - **Point 20:** The disclosures required by paragraph 16 shall include information about how the undertaking communicates its policies to those for whom they are relevant to ensure that the policy is accessible and that they understand its implications.
""",
'G1-3_21': """
   - **Point 21:** The disclosure required by paragraph 16 shall include information about the following with respect to training:
     - (a) the nature, scope and depth of anti- corruption and anti- bribery training programmes offered or required by the undertaking;
     - (b) the percentage of functions-at-risk covered by training programmes; and
     - (c) the extent to which training is given to members of the administrative, management and supervisory bodies.
""",
'G1-4_22': """
   - **Point 22:** The undertaking shall provide information on incidents of corruption or bribery during the reporting period.
""",
'G1-4_23': """
   - **Point 23:** The objective of this Disclosure Requirement is to provide transparency on the incidents relating to corruption or bribery during the reporting period and the related outcomes.
""",
'G1-4_24': """
   - **Point 24:** The undertaking shall disclose:
     - (a) the number of convictions and the amount of fines for violation of anti-corruption and anti- bribery ; and
     - (b) any actions taken to address breaches in procedures and standards of anti-corruption and anti-bribery;
""",
'G1-4_25': """
   - **Point 25:** The undertaking may disclose:
     - (a) the total number and nature of confirmed incidents of corruption or bribery;
     - (b) the number of confirmed incidents in which own workers were dismissed or disciplined for corruption or bribery-related incidents;
     - (c) the number of confirmed incidents relating to contracts with business partners that were terminated or not renewed due to violations related to corruption or bribery; and
     - (d) details of public legal cases regarding corruption or bribery brought against the undertaking and its own workers during the reporting period and the outcomes of such cases. This includes cases that were initiated in previous years where the outcome was only established in the current reporting period.
""",
'G1-4_26': """
   - **Point 26:** The disclosures required shall include incidents involving actors in its value chain only where the undertaking or its employees are directly involved.
""",
'G1_5_27': """
   - **Point 27:** The undertaking shall provide information on the activities and commitments related to exerting its political influence, including its lobbying activities related to its material impacts, risks and opportunities.
""",
'G1_5_28': """
   - **Point 28:** The objective of this Disclosure Requirement is to provide transparency on the undertaking’s activities and commitments related to exerting its political influence with political contributions, including the types and purpose of lobbying activities .
""",
'G1-5_29': """
   - **Point 29:** The disclosure required by paragraph 27 shall include:
     - (a) if applicable, the representative(s) responsible in the administrative, management and supervisory bodies for the oversight of these activities;
     - (b) for financial or in-kind political contributions:
        i.  the total monetary value of financial and in-kind political contributions made directly and indirectly by the undertaking aggregated by country or geographical area where relevant, as well as type of recipient/beneficiary; and
        ii. where appropriate, how the monetary value of in-kind contributions is estimated.
     - (c) the main topics covered by its lobbying activities and the undertaking’s main positions on these in brief. This shall include explanations on how this interacts with its material impacts, risks and opportunities identified in its materiality assessment per ESRS 2; and
     - (d) if the undertaking is registered in the EU Transparency Register or in an equivalent transparency register in a Member State, the name of any such register and its identification number in the register.
""",
'G1-5_30': """
   - **Point 30:** The disclosure shall also include information about the appointment of any members of the administrative, management and supervisory bodies who held a comparable position in public administration (including regulators) in the 2 years preceding such appointment in the current reporting period.
""",
'G1-6_31': """
   - **Point 31:** The undertaking shall provide information on its payment practices, especially with respect to late payments to small and medium enterprises (SMEs).
""",
'G1-6_32': """
   - **Point 32:** 	The objective of this Disclosure Requirement is to provide insights on the contractual payment terms and on its performance with regard to payment, especially as to how these impact SMEs and specifically with respect to late payments to SMEs.
""",
'G1-6_33': """
   - **Point 33:** The disclosure under paragraph 31 shall include:
     - (a) the average time the undertaking takes to pay an invoice from the date when the contractual or statutory term of payment starts to be calculated, in number of days;
     - (b) a description of the undertaking’s standard payment terms in number of days by main category of suppliers and the percentage of its payments aligned with these standard terms;
     - (c) the number of legal proceedings currently outstanding for late payments; and
     - (d) complementary information necessary to provide sufficient context. If the undertaking has used representative sampling to calculate the information required under point (a), it shall state that fact and briefly describe the methodology used.
""",
   }
   

disclosure_requirement_E1_1 = """
Disclosure Requirement **E1-1 – Transition plan for climate change mitigation**, ensure the response addresses:
"""

disclosure_requirement_E1_2 = """
Disclosure Requirement **E1-2 – Policies related to climate change mitigation and adaptation**, ensure the response addresses:
"""

disclosure_requirement_E1_3 = """
Disclosure Requirement **E1-3 – Actions and resources in relation to climate change policies**, ensure the response addresses:
"""

disclosure_requirement_E1_4 = """
Disclosure Requirement **E1-4 – Targets related to climate change mitigation and adaptation**, ensure the response addresses:
"""

disclosure_requirement_E1_5 = """
Disclosure Requirement **E1-5 – Energy consumption and mix**, ensure the response addresses:
"""

disclosure_requirement_E1_6 = """
Disclosure Requirement **E1-6 – Gross Scopes 1, 2, 3 and Total GHG emissions**, ensure the response addresses:
"""

disclosure_requirement_E1_7 = """
Disclosure Requirement **E1-7 – GHG removals and GHG mitigation projects financed through carbon credits**, ensure the response addresses:
"""

disclosure_requirement_E1_8 = """
Disclosure Requirement **E2-8 – Internal carbon pricing**, ensure the response addresses:
"""

disclosure_requirement_E1_9 = """
Disclosure Requirement **E1-9 – Anticipated financial effects from material physical and transition risks and potential climate-related opportunities**, ensure the response addresses:
"""

disclosure_requirement_E2_1 = """
Disclosure Requirement **E2-1 – Policies related to pollution**, ensure the response addresses:
"""

disclosure_requirement_E2_2 = """
For Disclosure Requirement **E2-2 – Actions and Resources Related to Pollution**, ensure the response addresses:
"""

disclosure_requirement_E2_3 = """
For Disclosure Requirement **E2-3 – Targets related to pollution**, ensure the response addresses:
"""

disclosure_requirement_E2_4 = """
For Disclosure Requirement **E2-4 – Pollution of air, water and soil**, ensure the response addresses:
"""

disclosure_requirement_E2_5 = """
For Disclosure Requirement **E2-5 – Substances of concern and substances of very high concern**, ensure the response addresses:
"""

disclosure_requirement_E2_6 = """
For Disclosure Requirement **E2-6 – Anticipated financial effects from material pollution-related risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_E3_1 = """
For Disclosure Requirement **E3-1 – Policies related to water and marine resources**, ensure the response addresses:
"""

disclosure_requirement_E3_2 = """
For Disclosure Requirement **E3-2 – Actions and resources related to water and marine resources**, ensure the response addresses:
"""

disclosure_requirement_E3_3 = """
For Disclosure Requirement **E3-3 – Targets related to water and marine resources**, ensure the response addresses:
"""

disclosure_requirement_E3_4 = """
For Disclosure Requirement **E3-4 – Water consumption**, ensure the response addresses:
"""

disclosure_requirement_E3_5 = """
For Disclosure Requirement **E3-5 – Anticipated financial effects from material water and marine resources-related risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_E4_1 = """
For Disclosure Requirement **E4_1 – Transition plan and consideration of biodiversity and ecosystems in strategy and business model**, ensure the response addresses:
"""

disclosure_requirement_E4_2 = """
For Disclosure Requirement **E4-2 – Anticipated financial effects from material water and marine resources-related risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_E4_3 = """
For Disclosure Requirement **E4-3 – Actions and resources related to biodiversity and ecosystems**, ensure the response addresses:
"""

disclosure_requirement_E4_4 = """
For Disclosure Requirement **E4-4 – Targets related to biodiversity and ecosystems**, ensure the response addresses:
"""

disclosure_requirement_E4_5 = """
For Disclosure Requirement **E4-5 – Impact metrics related to biodiversity and ecosystems change**, ensure the response addresses:
"""

disclosure_requirement_E4_6 = """
For Disclosure Requirement **E4-6 – Anticipated financial effects from material biodiversity and ecosystem-related risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_E5_1 = """
For Disclosure Requirement **E5-1 – Policies related to resource use and circular economy**, ensure the response addresses:
"""

disclosure_requirement_E5_2 = """
For Disclosure Requirement **E5-2 – Actions and resources related to resource use and circular economy**, ensure the response addresses:
"""
disclosure_requirement_E5_3 = """
For Disclosure Requirement **E5-3 – Targets related to resource use and circular economy**, ensure the response addresses:
"""

disclosure_requirement_E5_4 = """
For Disclosure Requirement **E5-4 – Resource inflows**, ensure the response addresses:
"""

disclosure_requirement_E5_5 = """
For Disclosure Requirement **E5-5 – Resource outflows**, ensure the response addresses:
"""

disclosure_requirement_E5_6 = """
For Disclosure Requirement **E5-6 – Anticipated financial effects from material resource use and circular economy-related risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_S1_1 = """
For Disclosure Requirement **S1-1 – Policies related to own workforce**, ensure the response addresses:
"""

disclosure_requirement_S1_2 = """
For Disclosure Requirement **S1-2 – Processes for engaging with own workforce and workers’ representatives about impacts**, ensure the response addresses:
"""

disclosure_requirement_S1_3 = """
For Disclosure Requirement **S1-3 – Processes to remediate negative impacts and channels for own workforce to raise concerns**, ensure the response addresses:
"""

disclosure_requirement_S1_4 = """
For Disclosure Requirement **S1-4 – Taking action on material impacts on own workforce, and approaches to managing material risks and pursuing material opportunities related to own workforce, and effectiveness of those actions**, ensure the response addresses:
"""

disclosure_requirement_S1_5 = """
For Disclosure Requirement **S1-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_S1_6 = """
For Disclosure Requirement **S1-6 – Characteristics of the undertaking’s employees**, ensure the response addresses:
"""

disclosure_requirement_S1_7 = """
For Disclosure Requirement **S1-7 – Characteristics of non-employees in the undertaking’s own workforce**, ensure the response addresses:
"""

disclosure_requirement_S1_8 = """
For Disclosure Requirement **S1-8 – Collective bargaining coverage and social dialogue**, ensure the response addresses:
"""

disclosure_requirement_S1_9 = """
For Disclosure Requirement **S1-9 – Diversity metrics**, ensure the response addresses:
"""

disclosure_requirement_S1_10 = """
For Disclosure Requirement **S1-10 – Adequate wages**, ensure the response addresses:
"""

disclosure_requirement_S1_11 = """
For Disclosure Requirement **S1-11 – Social protection**, ensure the response addresses:
"""

disclosure_requirement_S1_12 = """
For Disclosure Requirement **S1-12 – Persons with disabilities**, ensure the response addresses:
"""

disclosure_requirement_S1_13 = """
For Disclosure Requirement **S1-13 – Training and skills development metrics**, ensure the response addresses:
"""

disclosure_requirement_S1_14 = """
For Disclosure Requirement **S1-14 – Health and safety metrics**, ensure the response addresses:
"""

disclosure_requirement_S1_15 = """
For Disclosure Requirement **S1-15 – Work-life balance metrics**, ensure the response addresses:
"""

disclosure_requirement_S1_16 = """
For Disclosure Requirement **S1-16 – Remuneration metrics (pay gap and total remuneration)**, ensure the response addresses:
"""

disclosure_requirement_S1_17 = """
For Disclosure Requirement **S1-17 – Incidents, complaints and severe human rights impacts**, ensure the response addresses:
"""

disclosure_requirement_S2_1 = """
For Disclosure Requirement **S2-1 – Policies related to value chain workers**, ensure the response addresses:
"""

disclosure_requirement_S2_2 = """
For Disclosure Requirement **S2-2 – Processes for engaging with value chain workers about impacts**, ensure the response addresses:
"""

disclosure_requirement_S2_3 = """
For Disclosure Requirement **S2-3 – Processes to remediate negative impacts and channels for value chain workers to raise concerns**, ensure the response addresses:
"""

disclosure_requirement_S2_4 = """
For Disclosure Requirement **S2-4 – Taking action on material impacts on consumers and end- users, and approaches to managing material risks and pursuing material opportunities related to consumers and end-users, and effectiveness of those action**, ensure the response addresses:
"""

disclosure_requirement_S2_5 = """
For Disclosure Requirement **S2-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_S3_1 = """
For Disclosure Requirement **S3-1 – Policies related to affected communities**, ensure the response addresses:
"""

disclosure_requirement_S3_2 = """
For Disclosure Requirement **S3-2 – Processes for engaging with affected communities about impacts**, ensure the response addresses:
"""

disclosure_requirement_S3_3 = """
For Disclosure Requirement **S3-3 – Processes to remediate negative impacts and channels for affected communities to raise concerns**, ensure the response addresses:
"""

disclosure_requirement_S3_4 = """
For Disclosure Requirement **S3-4 – Taking action on material impacts on affected communities, and approaches to managing material risks and pursuing material opportunities related to affected communities, and effectiveness of those actions**, ensure the response addresses:
"""

disclosure_requirement_S3_5 = """
For Disclosure Requirement **S3-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_S4_1 = """
For Disclosure Requirement **S4-1 – Policies related to consumers and end-users**, ensure the response addresses:
"""

disclosure_requirement_S4_2 = """
For Disclosure Requirement **S4-2 – Processes for engaging with consumers and end-users about impacts**, ensure the response addresses:
"""

disclosure_requirement_S4_3 = """
For Disclosure Requirement **S4-3 – Processes to remediate negative impacts and channels for consumers and end-users to raise concerns**, ensure the response addresses:
"""

disclosure_requirement_S4_4 = """
For Disclosure Requirement **S4-4 – Taking action on material impacts on consumers and end- users, and approaches to managing material risks and pursuing material opportunities related to consumers and end-users, and effectiveness of those actions**, ensure the response addresses:
"""

disclosure_requirement_S4_5 = """
For Disclosure Requirement **S4-4 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities**, ensure the response addresses:
"""

disclosure_requirement_G1_1 = """
For Disclosure Requirement **G1-1 – Business conduct policies and corporate culture**, ensure the response addresses:
"""

disclosure_requirement_G1_2 = """
For Disclosure Requirement **G1-2 – Management of relationships with suppliers**, ensure the response addresses:
"""

disclosure_requirement_G1_3 = """
For Disclosure Requirement **G1-3 – Management of relationships with suppliers**, ensure the response addresses:
"""

disclosure_requirement_G1_4 = """
For Disclosure Requirement **G1-4 – Incidents of corruption or bribery**, ensure the response addresses:
"""

disclosure_requirement_G1_5 = """
For Disclosure Requirement **G1-5 – Political influence and lobbying activities**, ensure the response addresses:
"""

disclosure_requirement_G1_6 = """' = "
For Disclosure Requirement **G1-6 – Payment practices**, ensure the response addresses:
"""

_disclosure_requirement = {
    "E1-1": disclosure_requirement_E1_1,
    "E1-2": disclosure_requirement_E1_2,
    "E1-3": disclosure_requirement_E1_3,
    "E1-4": disclosure_requirement_E1_4,
    "E1-5": disclosure_requirement_E1_5,
    "E1-6": disclosure_requirement_E1_7,
    "E1-8": disclosure_requirement_E1_8,
    "E1-9": disclosure_requirement_E1_9,
    "E2-1": disclosure_requirement_E2_1,
    "E2-2": disclosure_requirement_E2_2,
    "E2-3": disclosure_requirement_E2_3,
    "E2-4": disclosure_requirement_E2_4,
    "E2-5": disclosure_requirement_E2_5,
    "E2-6": disclosure_requirement_E2_6,
    "E3-1": disclosure_requirement_E3_1,
    "E3-2": disclosure_requirement_E3_2,
    "E3-3": disclosure_requirement_E3_3,
    "E3-4": disclosure_requirement_E3_4,
    "E3-5": disclosure_requirement_E3_5,
    "E4-1": disclosure_requirement_E4_1,
    "E4-2": disclosure_requirement_E4_2,
    "E4-3": disclosure_requirement_E4_3,
    "E4-4": disclosure_requirement_E4_4,
    "E4-5": disclosure_requirement_E4_5,
    "E4-6": disclosure_requirement_E4_6,
    "E5-1": disclosure_requirement_E5_1,
    "E5-2": disclosure_requirement_E5_2,
    "E5-3": disclosure_requirement_E5_3,
    "E5-4": disclosure_requirement_E5_4,
    "E5-5": disclosure_requirement_E5_5,
    "E5-6": disclosure_requirement_E5_6,
    "S1-1": disclosure_requirement_S1_1,
    "S1-2": disclosure_requirement_S1_2,
    "S1-3": disclosure_requirement_S1_3,
    "S1-4": disclosure_requirement_S1_4,
    "S1-5": disclosure_requirement_S1_5,
    "S1-6": disclosure_requirement_S1_6,
    "S1-7": disclosure_requirement_S1_7,
    "S1-8": disclosure_requirement_S1_8,
    "S1-9": disclosure_requirement_S1_9,
    "S1-10": disclosure_requirement_S1_10,
    "S1-11": disclosure_requirement_S1_11,
    "S1-12": disclosure_requirement_S1_12,
    "S1-13": disclosure_requirement_S1_13,
    "S1-14": disclosure_requirement_S1_14,
    "S1-15": disclosure_requirement_S1_15,
    "S1-16": disclosure_requirement_S1_16,
    "S1-17": disclosure_requirement_S1_17,
    "S2-1": disclosure_requirement_S2_1,
    "S2-2": disclosure_requirement_S2_2,
    "S2-3": disclosure_requirement_S2_3,
    "S2-4": disclosure_requirement_S2_4,
    "S2-5": disclosure_requirement_S2_5,
    "S3-1": disclosure_requirement_S3_1,
    "S3-2": disclosure_requirement_S3_2,
    "S3-3": disclosure_requirement_S3_3,
    "S3-4": disclosure_requirement_S3_4,
    "S3-5": disclosure_requirement_S3_5,
    "S4-1": disclosure_requirement_S4_1,
    "S4-2": disclosure_requirement_S4_2,
    "S4-3": disclosure_requirement_S4_3,
    "S4-4": disclosure_requirement_S4_4,
    "S4-5": disclosure_requirement_S4_5,
    "G1-1": disclosure_requirement_G1_1,
    "G1-2": disclosure_requirement_G1_2,
    "G1-3": disclosure_requirement_G1_3,
    "G1-4": disclosure_requirement_G1_4,
    "G1-5": disclosure_requirement_G1_5,
    "G1-6": disclosure_requirement_G1_6
}

_discloure_requirement_title = {
    "E1-1": "E1-1 – Transition plan for climate change mitigation",
    "E1-2": "E1-2 – Policies related to climate change mitigation and adaptation",
    "E1-3": "E1-3 – Actions and resources in relation to climate change policies",
    "E1-4": "E1-4 – Targets related to climate change mitigation and adaptation",
    "E1-5": "E1-5 – Energy consumption and mix",
    "E1-6": "E1-7 – GHG removals and GHG mitigation projects financed through carbon credits",
    "E1-8": "E2-8 – Internal carbon pricing",
    "E1-9": "E1-9 – Anticipated financial effects from material physical and transition risks and potential climate-related opportunities",
    "E2-1": "E2-1 – Policies related to pollution",
    "E2-2": "E2-2 – Actions and Resources Related to Pollution",
    "E2-3": "E2-3 – Targets related to pollution",
    "E2-4": "E2-4 – Pollution of air, water and soil",
    "E2-5": "E2-5 – Substances of concern and substances of very high concern",
    "E2-6": "E2-6 – Anticipated financial effects from material pollution-related risks and opportunities",
    "E3-1": "E3-1 – Policies related to water and marine resources",
    "E3-2": "E3-2 – Actions and resources related to water and marine resources",
    "E3-3": "E3-3 – Targets related to water and marine resources",
    "E3-4": "E3-4 – Water consumption",
    "E3-5": "E3-5 – Anticipated financial effects from material water and marine resources-related risks and opportunities",
    "E4-1": "E4_1 – Transition plan and consideration of biodiversity and ecosystems in strategy and business model",
    "E4-2": "E4-2 – Anticipated financial effects from material water and marine resources-related risks and opportunities",
    "E4-3": "E4-3 – Actions and resources related to biodiversity and ecosystems",
    "E4-4": "E4-4 – Targets related to biodiversity and ecosystems",
    "E4-5": "E4-5 – Impact metrics related to biodiversity and ecosystems change",
    "E4-6": "E4-6 – Anticipated financial effects from material biodiversity and ecosystem-related risks and opportunities",
    "E5-1": "E5-1 – Policies related to resource use and circular economy",
    "E5-2": "E5-2 – Actions and resources related to resource use and circular economy",
    "E5-3": "E5-3 – Targets related to resource use and circular economy",
    "E5-4": "E5-4 – Resource inflows",
    "E5-5": "E5-5 – Resource outflows",
    "E5-6": "E5-6 – Anticipated financial effects from material resource use and circular economy-related risks and opportunities",
    "S1-1": "S1-1 – Policies related to own workforce",
    "S1-2": "S1-2 – Processes for engaging with own workforce and workers’ representatives about impacts",
    "S1-3": "S1-3 – Processes to remediate negative impacts and channels for own workforce to raise concerns",
    "S1-4": "S1-4 – Taking action on material impacts on own workforce, and approaches to managing material risks and pursuing material opportunities related to own workforce, and effectiveness of those actions",
    "S1-5": "S1-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities",
    "S1-6": "S1-6 – Characteristics of the undertaking’s employees",
    "S1-7": "S1-7 – Characteristics of non-employees in the undertaking’s own workforce",
    "S1-8": "S1-8 – Collective bargaining coverage and social dialogue",
    "S1-9": "S1-9 – Diversity metrics",
    "S1-10": "S1-10 – Adequate wages",
    "S1-11": "S1-11 – Social protection",
    "S1-12": "S1-12 – Persons with disabilities",
    "S1-13": "S1-13 – Training and skills development metrics",
    "S1-14": "S1-14 – Health and safety metrics",
    "S1-15": "S1-15 – Work-life balance metrics",
    "S1-16": "S1-16 – Remuneration metrics (pay gap and total remuneration)",
    "S1-17": "S1-17 – Incidents, complaints and severe human rights impacts",
    "S2-1": "S2-1 – Policies related to value chain workers",
    "S2-2": "S2-2 – Processes for engaging with value chain workers about impacts",
    "S2-3": "S2-3 – Processes to remediate negative impacts and channels for value chain workers to raise concerns",
    "S2-4": "S2-4 – Taking action on material impacts on consumers and end- users, and approaches to managing material risks and pursuing material opportunities related to consumers and end-users, and effectiveness of those action",
    "S2-5": "S2-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities",
    "S3-1": "S3-1 – Policies related to affected communities",
    "S3-2": "S3-2 – Processes for engaging with affected communities about impacts",
    "S3-3": "S3-3 – Processes to remediate negative impacts and channels for affected communities to raise concerns",
    "S3-4": "S3-4 – Taking action on material impacts on affected communities, and approaches to managing material risks and pursuing material opportunities related to affected communities, and effectiveness of those actions",
    "S3-5": "S3-5 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities",
    "S4-1": "S4-1 – Policies related to consumers and end-users",
    "S4-2": "S4-2 – Processes for engaging with consumers and end-users about impacts",
    "S4-3": "S4-3 – Processes to remediate negative impacts and channels for consumers and end-users to raise concerns",
    "S4-4": "S4-4 – Taking action on material impacts on consumers and end- users, and approaches to managing material risks and pursuing material opportunities related to consumers and end-users, and effectiveness of those actions",
    "S4-5": "S4-4 – Targets related to managing material negative impacts, advancing positive impacts, and managing material risks and opportunities",
    "G1-1": "G1-1 – Business conduct policies and corporate culture",
    "G1-2": "G1-2 – Management of relationships with suppliers",
    "G1-3": "G1-3 – Management of relationships with suppliers",
    "G1-4": "G1-4 – Incidents of corruption or bribery",
    "G1-5": "G1-5 – Political influence and lobbying activities",
    "G1-6": "G1-6 – Payment practices",
}

code_delimtter = '@'
def disclosure_requirement_points():
    return _disclosure_requirement_points

def disclosure_requirement(code: str):
    codes = code.split(code_delimtter)
    if len(codes) == 2:
        print(f"codes DR {codes[0]} point {codes[1]}")
    esrs_code = codes[0]
    esrs_code_points = json.loads(codes[1]) 
    print(esrs_code , esrs_code_points)
    dr_point_accumlated = ""
    for dr_point in esrs_code_points:
        dr_point_code = f"{esrs_code}_{dr_point}"
        print(esrs_code , dr_point_code)
        if dr_point_code in _disclosure_requirement_points:
            print({_disclosure_requirement_points[dr_point_code]})
            dr_point_accumlated = f"{dr_point_accumlated}\n{_disclosure_requirement_points[dr_point_code]}"
        else:
            print(f"Code not found {dr_point_code}")
            ##Raise Exception
    if esrs_code in _disclosure_requirement:
        dr = _disclosure_requirement[esrs_code]
        print(f"{dr}\n{dr_point_accumlated}")
        return f"_disclosure_requirement[esrs_code]"
    else:
        print(f"Code not found {esrs_code}")
        ##Raise Exception

def discloure_requirement_title(code: str):
    codes = code.split(code_delimtter)
    if len(codes) == 2:
        print(f"codes DR {codes[0]}")
    esrs_code = codes[0]
    if esrs_code in  _discloure_requirement_title:
        print(f"{_discloure_requirement_title[esrs_code]}")
    else:
        print(f"Code not found {code} {esrs_code}")

discloure_requirement_title("E1-1@[15]")