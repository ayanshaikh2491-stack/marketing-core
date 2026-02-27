from core.manager_router import route_manager
from core.output_filter import clean_output
from core.output_analyzer import refine_output
from core.report_saver import save_report


def handle_request(user_input: str) -> str:
    """
    Central execution pipeline.
    Flow:
    User → Manager → Agents → Filter → Analyzer → Save → Return
    """

    try:
        # Step 1 — Route to correct manager
        raw_output = route_manager(user_input)

        # Step 2 — Remove AI tone
        filtered_output = clean_output(raw_output)

        # Step 3 — Improve structure & quality
        final_output = refine_output(filtered_output)

        # Step 4 — Save report
        save_report(final_output)

        return final_output

    except Exception as e:
        return f"System Error: {str(e)}"
