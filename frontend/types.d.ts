
type ProjectResponse = {
    id: number;
    title: string;
    slug: string;
    limit_storage: number;
    current_storage: number;
    num_of_scenarios: number;
    user: number;
    created_at: string;
    updated_at: string;
};


type ScenarioResponse = {
    id: number;
    parent_id?: number | null;
    project: number;
    response?: number | null;
    user_details?: string | null;
    user: number;
    created_at: string;
    updated_at: string;
}