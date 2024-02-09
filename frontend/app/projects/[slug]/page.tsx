'use client';

import React, {useEffect, useState} from "react";
import {Tree, TreeNode} from 'react-organizational-chart';

interface PageParams {
	slug: string;
}

interface ResponseData {
	id: number;
	parent_id: number | null;
	response: string;
	user_details: string;
	user: number;
	created_at: string;
	updated_at: string;
}

export function getTree(projectSlug: string) {
	// eslint-disable-next-line react-hooks/rules-of-hooks
	const [tree, setTree] = useState<ResponseData[]>([]);

	// eslint-disable-next-line react-hooks/rules-of-hooks
	useEffect(() => {
		fetch(process.env.API_URL + `api/v1/scenario/tree/${projectSlug}`, {
			credentials: "include"
		})
			.then(response => response.json())
			.then(data => setTree(data));
	}, [projectSlug]);

	return tree
}

function constructTree(data: ResponseData[]) {
    const map = new Map<number, ResponseData>();
    const rootNodes: ResponseData[] = [];

    data.forEach(node => {
        map.set(node.id, node);
        node.children = [];
    });

    data.forEach(node => {
        const parent = map.get(node.parent_id || 0);
        if (parent) {
            parent.children.push(node);
        } else {
            rootNodes.push(node);
        }
    });

    return rootNodes;
}


export default function Page({ params }: { params: PageParams }) {
    const slug = params.slug;
    const treeData: ResponseData[] = getTree(slug);
    const tree = constructTree(treeData);

    const renderTreeNodes = (nodes: ResponseData[] | undefined) => {
        if (!nodes) return null;
        return nodes.map(node => (
            <TreeNode key={node.id} label={<div>{node.id}</div>}>
                {renderTreeNodes(node.children)}
            </TreeNode>
        ));
    };

    return (
        <main>
            <Tree label={<div>Root</div>}>
                {renderTreeNodes(tree)}
            </Tree>
        </main>
    );
}